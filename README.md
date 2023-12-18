[![](https://img.shields.io/maintenance/yes/2024)](https://github.com/jcivitel/)
[![GitHub issues](https://img.shields.io/github/issues/jcivitel/py_itu_change)](https://github.com/jcivitel/py_itu_change)
[![GitHub Repo stars](https://img.shields.io/github/stars/jcivitel/py_itu_change)](https://github.com/jcivitel/py_itu_change)
[![GitHub License](https://img.shields.io/github/license/jcivitel/py_itu_change)](https://github.com/jcivitel/py_itu_change)

# What is the goal of the project?

The problem of a telephony provider being audited annually by the Federal Network Agency and having to ensure that all number ranges in all countries are billed correctly is a complex challenge. This problem is particularly challenging because each country has implemented its own standard for publishing this information.

Each country has different number ranges and numbers formats. This ranges from different number lengths to specific prefixes for international calls. Each telephony provider must ensure that they apply the correct tariffs and billing rules for each country.

The goal is to have a list to automatically receive and retrieve the changes of the updates on the <a href="https://www.itu.int/oth/T0202.aspx?lang=en">ITU page</a> for the number ranges of all countries.

<br>

## How to install the project?
1. Begin by cloning the repository to a designated local directory on your machine.
```console
git clone https://github.com/jcivitel/py_itu_change.git
```
2. Launch a Command Prompt (CMD) and navigate to the specified directory. Once in the directory, execute the following command:
```python
python -m venv venv
```

3. Once the virtual Python environment has been successfully created, it is now possible to execute the script by the following steps:
```python
. venv/bin/activate
pip install -r reqirements.txt
python3 py_itu_change.py <date>
```

> [!NOTE]
> Note that you must replace `<date>` with the date (`YYYY-MM-DD`) from which you want to filter. All updates to the publications after this date will be taken into account.

<br>

## Example
```python
python3 py_itu_change.py 2023-10-01
```

### Output:
```python
--------------------------  ----------  --------------------------------------
Country                     Date        Link
--------------------------  ----------  --------------------------------------
Morocco                     2023-11-29  https://www.itu.int/oth/T0202000090/en
Senegal                     2023-11-29  https://www.itu.int/oth/T02020000B8/en
Mauritius                   2023-11-13  https://www.itu.int/oth/T0202000088/en
Nigeria                     2023-11-29  https://www.itu.int/oth/T020200009C/en
Uganda                      2023-11-13  https://www.itu.int/oth/T02020000F1/en
Burundi                     2023-11-29  https://www.itu.int/oth/T0202000022/en
Botswana                    2023-11-13  https://www.itu.int/oth/T020200001C/en
Iran (Islamic Republic of)  2023-11-29  https://www.itu.int/oth/T0202000066/en
--------------------------  ----------  --------------------------------------
8 countries have new updates
```

<br>

> [!TIP]
> You can also use the [Jenkinsfile](Jenkinsfile) in the project to carry out regular updates.

<br>

## Contributors
[![Contributors Display](https://badges.pufler.dev/contributors/jcivitel/garrysmod?size=50&padding=5&bots=false)](https://github.com/jcivitel/py_itu_change/graphs/contributors)
