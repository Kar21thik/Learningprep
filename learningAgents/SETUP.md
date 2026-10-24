# 📚 Learning Agents - Virtual Environment Setup

## Quick Start (One-time setup)

### Step 1: Create Virtual Environment

```bash
cd /Users/karthikr/Learning
python3 -m venv learning_env
```

### Step 2: Activate Virtual Environment

```bash
source learning_env/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r learningAgents/requirements.txt
```

### Step 4: Register Jupyter Kernel

```bash
python -m ipykernel install --user --name learning_agents --display-name "Learning Agents (Python 3.14)"
```

### Step 5: Start Jupyter

```bash
cd /Users/karthikr/Learning
jupyter notebook
```

### Step 6: Select the Right Kernel

When you open any notebook:
1. Click on "Kernel" menu
2. Select "Change kernel"
3. Choose "Learning Agents (Python 3.14)"

---

## Verify Installation

Run this in a notebook cell:

```python
import requests
import json
import boto3
import pandas as pd
import numpy as np

print("✓ All imports successful!")
print(f"✓ boto3 version: {boto3.__version__}")
print(f"✓ requests version: {requests.__version__}")
print(f"✓ pandas version: {pd.__version__}")
```

---

## Every Time You Want to Code

```bash
# Step 1: Activate virtual environment
cd /Users/karthikr/Learning
source learning_env/bin/activate

# Step 2: Start Jupyter
jupyter notebook

# Step 3: Select "Learning Agents" kernel in notebook
# (Kernel → Change kernel → Learning Agents)
```

---

## Troubleshooting

### ModuleNotFoundError: No module named 'boto3'

Make sure you:
1. ✓ Activated virtual environment (`source learning_env/bin/activate`)
2. ✓ Selected correct kernel in Jupyter (should show "Learning Agents" in top-right)
3. ✓ Installed requirements (`pip install -r learningAgents/requirements.txt`)

### Kernel not showing in Jupyter

Reinstall the kernel:
```bash
source learning_env/bin/activate
python -m ipykernel install --user --name learning_agents --display-name "Learning Agents (Python 3.14)"
```

### Still having issues?

```bash
# See all installed kernels
jupyter kernelspec list

# Remove broken kernel
jupyter kernelspec remove learning_agents

# Reinstall
python -m ipykernel install --user --name learning_agents --display-name "Learning Agents (Python 3.14)"
```

---

## Virtual Environment Deactivate

When you're done coding:
```bash
deactivate
```

This returns you to your system Python.

---

## What's Included?

- **jupyter** - Notebook environment
- **boto3** - AWS/DynamoDB SDK
- **requests** - HTTP requests library
- **pandas** - Data analysis
- **numpy** - Numerical computing
- **matplotlib** - Data visualization
- **ipykernel** - Jupyter kernel

---

## Next Steps

1. ✓ Virtual environment created
2. ✓ Kernel registered with Jupyter
3. ✓ Requirements.txt ready

**Now:** Open Chapter 1 notebook and start learning! 🚀
