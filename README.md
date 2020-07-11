# Python + Selene(Selenium wrapper) + Selenoid + Travis CI

[![Build Status](https://travis-ci.org/Oley96/ui-automation-demo.svg?branch=master)](https://travis-ci.org/Oley96/ui-automation-demo)

## How to start locally?
- clone repo
- start selenoid, selenoid-ui: docker-compose up -d
- run tests: pytest --browser_ver=83.0 tests/

## How to start with Travis CI?
- project should be on own GitHub
- on https://travis-ci.org/ activate current project
- make trigger commit and tests will run
