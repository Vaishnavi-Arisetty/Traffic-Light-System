# Traffic_Light_Signal

This project focuses on developing automatic traffic signal system.
It considers the presence of four way junction.
Taking all the signals in off condition, only the ones printed are turned on for each lane.

## __Running Test Coverages__
- The testing/ module has pytest unit tests.
- To run the complete coverage test : 
 `python -m coverage run -m pytest test`
- To run specific sub-test module : 
 `python -m coverage run -m pytest test/<folder/file name of the test>`
- To output the report for the previously run coverage tests: 
`coverage report --omit=<environment_folder_name>/*`
- To export the report in HTML:
`coverage html --omit=<environment_folder_name>/*`

