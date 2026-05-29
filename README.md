# Anatomy

本目录用于练习使用 PyVista 读取和展示三维解剖模型。

## 文件说明

- `attempt.py`：最小示例脚本，读取本地 `skull.stl` 并调用 PyVista 进行三维展示。
- `pics.ipynb`：交互式实验 notebook，用于记录三维模型读取、展示和可视化尝试。

## 数据说明

`skull.stl` 属于本地三维模型数据文件，通常体积较大或来源受限，因此不纳入 Git 版本管理。运行脚本前需要将对应 STL 文件放在本目录下。

## 运行方式

```bash
cd Anatomy
python attempt.py
```

如果使用独立虚拟环境，请先安装 PyVista 及其可视化依赖。
