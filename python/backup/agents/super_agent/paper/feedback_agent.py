#!/usr/bin/envs python3
# -*- coding: utf-8 -*-
import json
from dora import DoraStatus
import pyarrow as pa

from mofa.kernel.utils.log import write_agent_log
from mofa.kernel.utils.util import load_agent_config
from mofa.run.run_agent import run_dspy_agent, run_crewai_agent



class Operator:
    def on_event(
            self,
            dora_event,
            send_output,
    ) -> DoraStatus:
        if dora_event["type"] == "INPUT":
            if dora_event['id'] == 'writer_report' or dora_event['id'] == 'evaluation_result' or dora_event['id'] == 'evaluation_result':
                inputs = load_agent_config('use_case/feedback_agent.yml')
                writer_result = json.loads(dora_event["value"][0].as_py())
                print('writer_result  :  ',writer_result)

                inputs['context'] = writer_result.get('context')
                max_iterations,local_iterations = inputs.get('max_iterations'),writer_result.get('local_iterations', None)

                if local_iterations!=1 and  max_iterations >= local_iterations :
                    return DoraStatus.STOP

                rag_data =  writer_result.get('rag_data',None)
                print('inputs  :  ',inputs)

                if 'agents' not in inputs.keys():
                    inputs['task'] = writer_result['task']
                    result = run_dspy_agent(agent_config=inputs)
                else:
                    result = run_crewai_agent(crewai_config=inputs)
                if inputs.get('max_iterations',None) is not None:

                    result = {'task':writer_result.get('task'),'suggestion':result,'context':writer_result.get('context'),'local_iterations':writer_result.get('local_iterations', None),'rag_data':rag_data}
                else:
                    result = {'task':writer_result.get('task'),'suggestion':result,'context':writer_result.get('context'),'rag_data':rag_data}

                print(result)
                log_result = {"5, " + inputs.get('log_step_name', "Step_one"): result['suggestion']}
                write_agent_log(log_type=inputs.get('log_type', None), log_file_path=inputs.get('log_path', None),
                                data=log_result)
                send_output("feedback_result", pa.array([json.dumps(result)]),dora_event['metadata'])  # add this line
        return DoraStatus.CONTINUE


inputs = load_agent_config('use_case/feedback_agent.yml')