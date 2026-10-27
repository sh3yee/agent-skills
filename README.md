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

## 维护方式

1. 在本仓库的相应分类目录中修改技能。
2. 检查规则一致性、引用路径及相关脚本，通过 Git 查看和记录差异。
3. 只有用户明确要求安装或同步时，才按目标工具要求将指定技能部署到对应位置，并检查工具依赖及兼容性。

本仓库是独立副本，未与任何已安装技能目录建立软链接或自动同步。这里的分类结构用于源码管理；实际安装布局以目标工具要求为准。
