# Continuous Machine Learning for Layman Brothers Classification problem

This small project was shamelessly forked from the CML Repo made by [Elle O'Brien](https://elle-obrien.com/) ([andronovhopf](https://github.com/andronovhopf))

## About this Toy Project
The point of this repo it's create a small toy project for Machine Learning Operations (MLOps) or DevOps for Data.

Most of the general concepts about it can be found in this article from [Elle O'Brien](https://elle-obrien.com/) called [What data scientists need to know about DevOps](https://towardsdatascience.com/what-data-scientists-need-to-know-about-devops-2f8bc6660284).

## Install
1. Fork this repository
2. Create a new git branch for experimenting using the following command:
```bash
$ git checkout -b "tuning-decrease-depth"
```
In that case we're going to call our branch of `"tuning-decrease-depth"` because we're going to simulate an new experiment with a new parameter
3. Open the file `cml_layman_brothers/src/main/processing/train.py`
4. Change the parameter `depth` using any number. In this example, let's use `depth = 7`
5. Now add, commit and push your changes, using the following command:
```bash
$ git add .
$ git commit -m "Tuning - Decrease depth from 25 to 7"
$ git push origin tuning-decrease-depth
```
6. As soon as GitHub detects the push, GitHub deploys one of their computers to run the functions in your `.yaml`.
4. GitHub returns a notification if the functions ran successfully or not.



## Operational Systems

I tested in the following setups and all of them worked.

- **Operating system**: macOS Catalina · Linux · Windows
- **Python version**: 3.5+ (only 64 bit)
- **Package managers**: [pip]


## What a hell is this `cml.yaml` doing?
This file is stored inside of `.github/workflows/cml.yaml` and it's used to automate workflows inside of [GitHub Actions](https://docs.github.com/en/actions/configuring-and-managing-workflows/configuring-a-workflow).

In that way all lifecycle of any application can be automated for every Pull Request. Flows like Build, test, and deploy can be implemented inside [GitHub Actions](https://docs.github.com/en/actions/configuring-and-managing-workflows/configuring-a-workflow) only using this file, allowing us in this small project have a CI/CD in our experiments.

Street Fight explanation of the `.github/workflows/cml.yaml` file:
```yaml
# Workflow name
name: model-training

# This workflow is triggered on pushes to the repository.
on: [push]


jobs:
  run:
    # Uses the last image compiled from Ubuntu available in the Github Actions Marketplace
    runs-on: [ubuntu-latest]

    # CML Docker image with Python 3 will be pulled by the GitHub Actions runner
    container: docker://dvcorg/cml-py3:latest

    # What this Github "Action" will do
    steps:
      # This step uses GitHub's actions/checkout
      - uses: actions/checkout@v2
      - name: cml_run

        # Environment Variables used (in my case only my Github Token)
        env:
          repo_token: ${{ secrets.GITHUB_TOKEN }}

        # Steps that will be ran
        run: |

        # Will install the requirements
          pip install -r requirements.txt

          # Small test to check if all requirements are installed. Will break if something isn't right.
          python3.6 -m pytest cml_layman_brothers/src/test/unit_test/test_requirements.py -o log_cli=true --log-cli-level=INFO

          # Unit tests
          pytest cml_layman_brothers/src/test/unit_test/test_data_extraction.py -o log_cli=true --log-cli-level=INFO

          # Execute the Data Extraction script
          python cml_layman_brothers/src/main/processing/data_extraction.py

          # Execute the Training script
          python cml_layman_brothers/src/main/processing/train.py

          # Will get the "metrics.txt" file (generated in the training) and will get the model accuracy and will put inside of the report.md that is the file that will be used in the Pull Request for Code Review
          cat cml_objects/metrics.txt >> report.md

          # Will get the "confusion_matrix.png" file (guess what: generated in the training) and will get the confusion matrix and will put inside of the report.md that is the file that will be used in the Pull Request for Code Review
          cml-publish cml_objects/confusion_matrix.png --md >> report.md

          # Will send any kind of comment to the "report.md"
          cml-send-comment report.md

          # Will delete the data inside the Docker container
          python cml_layman_brothers/src/main/processing/data_cleanup.py
```

## Things in place

- Logging in all scripts
- Testing using PyTest
- Unit Tests
- Requirements check


## Run Tests
Check if all requirements are installed
```bash
$ python3.6 -m pytest \
cml_layman_brothers/src/test/unit_test/test_requirements.py -o \
log_cli=true --log-cli-level=INFO
```

Unit Tests for the `data_extraction.py` script
```bash
$ python3.6 -m pytest \
cml_layman_brothers/src/test/unit_test/test_data_extraction.py -o \
log_cli=true --log-cli-level=INFO
```

## TODO
- [ ] Experiment Branching
- [ ] Decent Unit Testing Data
- [ ] Decent Unit Testing Code
- [ ] More Logging
- [ ] Dump Training Logs
- [ ] Model serialization
- [ ] Include `black` linter in the pipeline
- [ ] Decent Data Pipeline
- [ ] Decent graphs and analysis in the PR
- [ ] Integration Test using holdout data
