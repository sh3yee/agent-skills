---
name: vue-project-style
description: Vue 项目开发、重构和排错的入口技能。处理 Vue 任务时先读取本技能，确认项目约定，再按需读取 Vue 最佳实践与专项技能。
---

# Vue 项目约定

## 技能协作

- 通用 Vue 实践遵循 [vue-best-practices](../vue-best-practices/SKILL.md)，本技能补充项目偏好与执行约定。
- 按任务读取专项技能及必要参考文件，不默认加载全部技能：
  - 运行错误、响应式或异步问题：[vue-debug-guides](../vue-debug-guides/SKILL.md)。
  - 路由与导航：[vue-router-best-practices](../vue-router-best-practices/SKILL.md)。
  - Pinia 状态管理：[vue-pinia-best-practices](../vue-pinia-best-practices/SKILL.md)。
  - 测试实现与排查：[vue-testing-best-practices](../vue-testing-best-practices/SKILL.md)。
  - 需要兼容普通值、ref、getter 输入的组合式函数：[create-adaptable-composable](../create-adaptable-composable/SKILL.md)。
  - JSX / TSX：[vue-jsx-best-practices](../vue-jsx-best-practices/SKILL.md)。
  - 维护 Options API 代码：[vue-options-api-best-practices](../vue-options-api-best-practices/SKILL.md)。
- 用户明确要求优先；这些 Vue 技能之间，项目风格、测试与执行约定以本技能为准。技术指导不扩大任务范围或执行权限。

## 项目设计偏好

- 遵循 Less is more：优先复用现有组件、hook、Store、工具、API 封装和样式，用直白实现减少概念与层级；最小改动仍需完成必要的职责拆分。
- 修改关联流程时，特别检查历史记录和持久化；需要改变对外接口、数据结构或调用方式时，先说明影响范围。
- 处理外部数据、跨窗口消息和远程组件时，在实际边界进行类型判断、参数校验、错误处理及必要的状态恢复。
- 同一能力需要跨界面、消息和执行流程保持一致时，使用统一能力判断，按需采用集合、映射或嵌套配置；简单独立开关保持简单。限制应覆盖实际执行入口，且不擅自扩展到未授权的后端层级。

## 代码风格

- 使用 PowerShell / Windows 命令；项目技术栈为 Vue + TypeScript + Naive UI。
- `<script setup>` 中的局部函数优先使用 `const xxx = () => {}`，事件处理函数使用 `handleXxx` 命名；Options API 的 `methods` 和生命周期遵循其 `this` 绑定要求。
- 优先使用提前返回降低嵌套，使用语义清晰的命名。
- 仅为关键业务规则、数据边界、兼容处理、异步流程和风险点添加简短中文注释。
- `<script setup>` 内同类声明集中放置，默认顺序为：imports → 类型 → 常量 → props / emits → reactive state / ref → computed → methods / functions → watchers / watchEffect → 生命周期与卸载逻辑。项目已有明确约定时沿用；初始化依赖优先于排序，避免在 `const` 函数初始化前调用它。
- 使用项目现有 Prettier 配置。

## 测试与验证

- 除非用户明确要求编写或保留测试代码，不在项目中新增或保留测试文件、测试脚本、测试夹具或专门用于测试的业务代码。
- 可以运行已有测试；临时测试优先放在临时目录，结束后清理本次创建的文件及产物，不把临时测试代码和命令写入交付代码或文档。
- 不删除项目原有测试或用户要求保留的测试。

## 执行边界

- 未经用户明确要求，不新增依赖。用户要求新增依赖时，可修改依赖声明和必要代码并提供安装命令；只有用户明确要求代为安装、升级或卸载时，才执行对应操作。
- 不代替用户启动程序，不运行 dev、serve、preview；需要启动时提供命令。
- 不代替用户构建程序，不运行 build；需要构建验证时提供命令。
- 不主动运行完整 type-check，只有用户在当前请求中明确要求时才运行。
