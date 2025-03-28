# 如何在比赛中使用 AWS Notebook 运行案例和提交代码

本文档旨在帮助参赛者，特别是新手，了解如何在比赛中使用在线 `Notebook` 环境运行案例代码并提交项目。

## 目录

1. [注册 SiliconFlow](#1-注册-siliconflow)
2. [访问 AWS Notebook 环境](#2-访问-aws-notebook-环境)
    - [2.1 获取 Notebook 网址和登录密钥](#21-获取-notebook-网址和登录密钥)
    - [2.2 登录 Notebook 环境](#22-登录-notebook-环境)
3. [比赛代码的创建和运行](#3-比赛代码的创建和运行)
    - [3.1 克隆项目代码](#31-克隆项目代码)
    - [3.2 更新代码环境](#32-更新代码环境)
    - [3.3 运行示例代码](#33-运行示例代码)
4. [创建和提交代码](#4-创建和提交代码)
    - [4.1 配置 Git 访问令牌和用户信息](#41-配置-git-访问令牌和用户信息)
    - [4.2 创建案例](#42-创建案例)
    - [4.3 确保提交案例的结构](#43-确保提交案例的结构)
    - [4.4 提交代码](#44-提交代码)
        - [4.4.1 提交代码到远程仓库](#441-提交代码到远程仓库)
        - [4.4.2 提交 Pull Request（PR）](#442-提交-pull-requestpr)
    - [4.5 提交案例流程总结](#45-提交案例流程总结)
5. [常见问题及解决方法](#5-常见问题及解决方法)
6. [附录](#6-附录)

---

## 1. 注册 SiliconFlow

请前往 [SiliconFlow 注册页面](../siliconflow_llms.md) 注册账户，以获取 LLM 密钥。

---

## 2. 访问 AWS Notebook 环境

### 2.1 获取 Notebook 网址和登录密钥

1. **获取登录信息**：

    - 组委会将为每位参赛者提供一个专属的 Notebook 网址和登录密钥。
    - 请查收您的邮箱或参赛通知，以获取这些信息。

### 2.2 登录 Notebook 环境

1. **访问 Notebook 网址**：

    - 在浏览器中输入您获得的 Notebook 网址。

2. **输入登录密钥**：

    - 在登录页面，输入组委会提供的登录密钥。
    - 点击 **登录** 按钮，进入 Notebook 环境。

3. **熟悉环境**：

    - 登录成功后，您将进入 Jupyter Notebook 界面。
    - 您可以在这里创建、编辑和运行代码。

---

## 3. 比赛代码的创建和运行

### 3.1 克隆项目代码

1. **Fork 比赛项目**：

    - 登录 GitCode，访问比赛官方的项目仓库：[https://gitcode.com/moxin-org/mofa](https://gitcode.com/moxin-org/mofa)。
    - 点击 **Fork** 按钮，将官方仓库复制到您的个人或团队仓库中。

2. **克隆仓库到 Notebook 环境**：

    - 在 Notebook 的界面，点击右上角的 **New** 按钮，选择 **Terminal**，打开终端。

    - 在终端中，运行以下命令克隆仓库：

    ```bash
    git clone https://gitcode.com/您的用户名/mofa.git
    ```

    - 克隆成功后，当前目录下会创建一个名为 `mofa` 的文件夹。

### 3.2 更新代码环境

1. **进入项目目录**：

    ```bash
    cd {project_name}/python
    ```

2. **更新依赖包**：

    ```bash
    pip3 install -e .
    ```

    > **说明**：该命令会根据 `setup.py` 文件安装项目的依赖包。

### 3.3 运行示例代码

1. **运行示例**：

    - 在 `{project_name}/python/examples` 目录下，有一些示例代码供参考。
    - 您可以在 Notebook 界面中打开这些示例，尝试运行，确保环境配置正确。

2. **验证环境**：

    - 确认示例代码运行无误，表示环境已正确配置，可以开始进行开发。

---

## 4. 创建和提交代码

### 4.1 配置 Git 访问令牌和用户信息

1. **创建访问令牌**：

    - 在 GitCode 右上角，点击 **头像**，选择 **个人设置**。
    - 进入 **安全设置**，找到 **访问令牌** 选项，点击 **新建访问令牌**。
    - 设置令牌的描述（例如：“比赛提交令牌”）和到期时间，然后点击 **创建访问令牌**。
    - **复制生成的访问令牌**，并妥善保存，稍后提交代码时需要使用。

2. **配置 Git 用户信息**：

    ```bash
    git config --global user.name "您的姓名"
    git config --global user.email "您的邮箱地址"
    ```

    > **提示**：确保用户名和邮箱与您的 GitCode 账户信息一致。

### 4.2 创建案例

1. **创建案例目录**：

    ```bash
    cd {project_name}/Hackathon/projects
    mkdir 您的团队名称
    cd 您的团队名称
    ```

2. **编写代码**：

    - 在您的团队目录下，编写或修改代码，确保代码结构清晰。

3. **完善 README.md 文件**：

    ```bash
    vim README.md
    ```

    - 简要说明您的案例内容和功能。

### 4.3 确保提交案例的结构

1. **案例结构要求**：

    - 提交的案例结构应与 `examples` 目录下的原有案例结构一致，包含以下内容：

        - `configs/*.yml`：配置文件，定义配置的结构。
        - `scripts/*.py`：包含 `dora-node` 和操作符的脚本文件。
        - `案例名称_dataflow.yml`：`dora-dataflow` 的文件。
        - `README.md`：如何编辑自己的 `README.md` 文件。示例参考：[sample_readme](sample_readme.md)
        - `案例_dataflow-graph.html`：使用 Dora Graph 生成的 dataflow 展示结构。
        - `agent_response.json`：用于保存您的 agent 的任务和结果，内容结构为：
        - `data/input/*` ：用来保存这个`Dora-Dataflow`需要的输入数据
        - `data/output/agent_response.json`：用来保存这个`Dora-Dataflow`的输出数据.要求格式如下.其中task代表你至少要执行的任务，response代表你的agent的输出结果
            ```json
           [
            {
                "task": "你是谁?",
                "response": "Hello World"
            },
            {
                "task": "你的名字是什么?",
                "response": "Hello World"
            }
          ]
          ```
        - `data/info/[team.jpg｜personal.jpg]` ： 个人或者团队照片
        - `data/info/[team.md｜personal.md]` ： 个人或者团队成员说明
        - `data/info/ExplanatoryVideo.mp4` : 
            - **分辨率：**1080p 或 2K。
            - **文件大小：**最大限制 150MB。
            - **时长：**3-5 分钟。
            - **录制工具：**使用腾讯会议或 OBS 进行视频录制。
            - **内容要求：**
              - 根据你的README来进行演讲
              - 需要在视频中运行你的项目.必须完整的看到你的项目从依赖安装启动以及运行结束的流程
    
2. **提交注意事项**：
  - **不要上传您的 API 密钥**。在 `git push` 之前，请仔细检查上传的文件中不包含任何密钥信息。
  - **不要修改非 examples 目录之外的源码**。如果您发现仓库中的代码存在问题，请联系组委会进行处理。若您修改了非 examples 的代码，我们会拒绝合并您的 PR。
  - 如果您的案例需要安装其他的包，请将这些依赖包添加到 `requirements.txt` 中。
  - 如果您的案例需要特殊的安装或运行步骤，请在 `README.md` 中详细说明，包括安装和运行的流程。

3. **项目打包发送给组委会**：
  - 参赛选手务必将自己的项目进行打包并且发送给组委会
    ~~~
    sudo apt update
    sudo apt install zip
    cd /examples 
    zip -r you_project.zip you_project/
    用户自行添加 `gitcode君`微信号 然后私聊将文件发给他
    ~~~

### 4.4 提交代码

#### 4.4.1 提交代码到远程仓库

1. **添加更改**：

    ```bash
    git add .
    ```

2. **提交更改并添加提交信息**：

    ```bash
    git commit -m "添加 [个人/团队名称] 的案例"
    ```

3. **设置远程仓库的 URL（包含访问令牌）**：

    ```bash
    git remote set-url origin https://您的用户名:您的访问令牌@gitcode.com/您的用户名/mofa.git
    ```

    > **示例**：

    ```bash
    git remote set-url origin https://johnDoe:abcdef123456@gitcode.com/johnDoe/mofa.git
    ```

4. **推送代码到远程仓库**：

    ```bash
    git push origin main
    ```

    > **注意**：

    - 将 `您的用户名`、`您的访问令牌` 和 `mofa` 替换为实际信息。
    - 如果默认分支不是 `main`，请使用相应的分支名称（例如 `master`）。

#### 4.4.2 提交 Pull Request（PR）

1. **提交 PR**：

    - 在您 Fork 的仓库页面，点击 **New Pull Request** 按钮。

2. **填写 PR 信息**：

    - 在 PR 描述中，详细说明您提交的内容，包括：

        - **提交的内容**：添加或修改了哪些文件和功能。
        - **逻辑说明**：代码实现的逻辑和工作方式。
        - **修改原因**：如果修改了现有代码，说明原因和解决的问题。

    - 确认无误后，点击 **Create Pull Request** 提交 PR。

    > **示例描述**：

    ```
    ### 提交内容
    - 添加了 `configs/sample_config.yml` 配置文件。
    - 编写了 `scripts/sample_script.py` 脚本，实现数据处理功能。

    ### 逻辑说明
    - `sample_script.py` 读取配置文件中的参数，处理输入数据并生成输出结果。

    ### 修改原因
    - 修正了原有脚本中的数据读取错误，确保数据处理的准确性。
    ```

    - 提交 PR 后，您的修改将被官方仓库审查，审核通过后会合并到主项目中。

### 4.5 提交案例流程总结

1. **确保案例结构正确**：

    - 在提交代码之前，确保您的案例符合要求的目录结构和文件规范。

2. **提交代码到远程仓库**：

    - 按照上述步骤，将代码提交并推送到您的 GitCode 仓库。

3. **提交 Pull Request（PR）**：

    - 在您 Fork 的仓库页面，点击 **New Pull Request** 按钮，提交您的修改。

---

## 5. 常见问题及解决方法

### 5.1 无法登录 Notebook 环境

- **解决方法**：

    - 确认您使用了正确的 Notebook 网址和登录密钥。
    - 检查网络连接是否正常。
    - 如果仍有问题，请联系组委会获取帮助。

### 5.2 无法登录 GitCode

- **解决方法**：

    - 确认网络连接正常。
    - 检查用户名和密码是否正确。
    - 如果忘记密码，可以通过 **找回密码** 功能重置。

### 5.3 访问令牌丢失或泄露

- **解决方法**：

    - 如果访问令牌丢失，请重新创建新的访问令牌。
    - 确保令牌保存在安全的地方，避免泄露。

### 5.4 克隆仓库失败

- **解决方法**：

    - 确认仓库 URL 是否正确。
    - 检查是否配置了正确的访问令牌（如需要）。
    - 确认网络连接正常。

### 5.5 提交代码遇到冲突

- **解决方法**：

    - 拉取最新的远程仓库代码：

    ```bash
    git pull origin main
    ```

    - 解决代码冲突后，重新提交代码。

### 5.6 更多问题

- **解决方法**：

    - 请参阅 [常见问题解答 (FAQ)](../frequently_asked_questions_(faq).md)。

---

## 6. 附录

- **Git 基础知识**：

    - 如果您对 Git 不熟悉，建议先学习一些基础知识，如 [Git 官方文档](https://git-scm.com/doc)。

- **GitCode 帮助中心**：

    - 更多关于 GitCode 的使用，可以参考 [GitCode 帮助中心](https://gitcode.net/help)。



