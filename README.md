# Agent Skills

按领域维护的个人 AI agent 技能源代码仓库，用于评估、修改和扩展技能，不绑定特定工具。

## 目录

```text
agent-skills/
  vue/
    create-adaptable-composable/
    vue-best-practices/
    vue-debug-guides/
    vue-jsx-best-practices/
    vue-options-api-best-practices/
    vue-pinia-best-practices/
    vue-project-style/
    vue-router-best-practices/
    vue-testing-best-practices/
  git/
    git-weekly-report/
```

每个类别放在 `<category>/`，每个技能放在 `<category>/<skill-name>/`，包含 `SKILL.md` 和所需的参考文档、脚本、资源。新增领域时增加对应分类目录；同类技能放在一起。

## 来源与范围

- 初始导入日期：2026-10-27。
- 初始来源目录：`C:\Users\she\.codex\skills`。这只是导入来源，不代表仓库绑定该工具。
- 当前保留 Vue 和 Git 类技能，不维护 Figma 类技能。
- 不纳入运行工具管理的系统技能或插件缓存。
- 分类整理保留技能原始内容、支持文件，以及第三方作者和许可声明。
- 8 个上游 Vue 技能来自 [vuejs-ai/skills](https://github.com/vuejs-ai/skills)，遵循 [MIT 许可](vue/LICENSE.vuejs-ai)；`vue-project-style` 由本仓库自行维护。

## 维护方式

1. 在本仓库的相应分类目录中修改技能。
2. 检查规则一致性、引用路径及相关脚本，通过 Git 查看和记录差异。
3. 只有用户明确要求安装或同步时，才按目标工具要求将指定技能部署到对应位置，并检查工具依赖及兼容性。

本仓库是独立副本，未与任何已安装技能目录建立软链接或自动同步。这里的分类结构用于源码管理；实际安装布局以目标工具要求为准。

## 定期更新 Vue 技能

[Sync Vue skills](.github/workflows/sync-vue-skills.yml) 每周一 09:23（Asia/Taipei，UTC+8）检查上游 `main` 分支，也支持在 GitHub Actions 页面通过 **Run workflow** 手动触发。定时任务可能因 GitHub 调度而延迟。

有内容变化时，工作流会向默认分支创建或更新同一个 PR（分支为 `automation/sync-vue-skills`），检查差异后手动合并；没有变化则不创建 PR。

同步范围固定为现有的 8 个上游技能：

- `create-adaptable-composable`
- `vue-best-practices`
- `vue-debug-guides`
- `vue-jsx-best-practices`
- `vue-options-api-best-practices`
- `vue-pinia-best-practices`
- `vue-router-best-practices`
- `vue-testing-best-practices`

这些目录会完整跟随上游，包括删除过期文件；个性化规则请放在 `vue-project-style`。工作流同时更新上游许可文件，保留技能中的作者声明，不自动导入上游新增技能，也不操作本机已安装技能目录。

工作流使用 GitHub 自动提供的 `GITHUB_TOKEN`，无需账户密码、个人访问令牌或 SSH Secret。首次使用需在 **Settings → Actions → General → Workflow permissions** 勾选 **Allow GitHub Actions to create and approve pull requests**；所需的 `contents: write` 和 `pull-requests: write` 已在工作流中声明。

同步脚本为 [scripts/sync_vue_skills.py](scripts/sync_vue_skills.py)，仅使用 Python 标准库。上游缺少任一指定技能或许可文件时，会在修改目录前失败，便于检查上游结构变化。
