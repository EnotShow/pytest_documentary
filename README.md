<center><h1>Pytest documentary</h1></center>
<center><h2>v0.1.0</h2></center>

<center><h6>Pytest plugin for simple test documentation</h6></center>

Usage:

```
pip install pytest-documentary
```
Run the pytest with --pytest-documentary flag
```
pytest --pytest-documentary
```

You can use additional flags:
```
pytest --pytest-documentary --documentary-output-file documentary_output.xls --documentary-output-path ./results/
```

<b>pytest.ini</b>
```
[pytest]
# Enable or disable the plugin by default
documentary-enabled = true  # Change to true to enable by default
# Default output file name
documentary-output-file = documentary_output.xlsx
# Default output path
documentary-output-path = ./
```