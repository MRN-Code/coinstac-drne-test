#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 21:59:06 2018

@author: Harshvardhan
"""

# input to local_1
python local.py '{"input":{"covariates":[[2,3],[3,4],[7,8],[7,5],[9,8]], "dependents":[6,7,8,5,6], "lambda":0}, "cache":{}}'

# output from local_1
'{"output": {"XtransposeX_local": [[5.0, 28.0, 28.0], [28.0, 192.0, 181.0], [28.0, 181.0, 178.0]], "Xtransposey_local": [32.0, 178.0, 183.0], "mean_y_local": 6.4, "count_local": 5, "computation_phase": "local_1"}, "cache": {"covariates": [[2, 3], [3, 4], [7, 8], [7, 5], [9, 8]], "dependents": [6, 7, 8, 5, 6], "lambda": 0}}'

# inpput to remote_1
python remote.py '{"input": {"local0": {"XtransposeX_local": [[5.0, 28.0, 28.0], [28.0, 192.0, 181.0], [28.0, 181.0, 178.0]], "Xtransposey_local": [32.0, 178.0, 183.0], "mean_y_local": 6.4, "count_local": 5, "computation_phase": "local_1"}}, "cache": {"covariates": [[2, 3], [3, 4], [7, 8], [7, 5], [9, 8]], "dependents": [6, 7, 8, 5, 6], "lambda": 0}}'

# output from remote_1
'{"cache": {"avg_beta_vector": [4.816936488169361, -0.7310087173100862, 1.0136986301369817], "mean_y_global": 6.4, "dof_global": 2}, "output": {"avg_beta_vector": [4.816936488169361, -0.7310087173100862, 1.0136986301369817], "mean_y_global": 6.4, "computation_phase": "remote_1"}}'

# input to local_2
python local.py '{"cache": {"covariates": [[2, 3], [3, 4], [7, 8], [7, 5], [9, 8]], "dependents": [6, 7, 8, 5, 6], "lambda": 0}, "input": {"avg_beta_vector": [4.816936488169361, -0.7310087173100862, 1.0136986301369817], "mean_y_global": 6.4, "computation_phase": "remote_1"}}'


# output from local_2
'{"output": {"SSE_local": 0.47073474470734844, "SST_local": 5.2, "varX_matrix_local": [[5.0, 28.0, 28.0], [28.0, 192.0, 181.0], [28.0, 181.0, 178.0]], "computation_phase": "local_2"}}'

# input to remote_2
python remote.py '{"input": {"local0": {"SSE_local": 0.47073474470734844, "SST_local": 5.2, "varX_matrix_local": [[5.0, 28.0, 28.0], [28.0, 192.0, 181.0], [28.0, 181.0, 178.0]], "computation_phase": "local_2"}}, "cache": {"avg_beta_vector": [4.816936488169361, -0.7310087173100862, 1.0136986301369817], "mean_y_global": 6.4, "dof_global": 2}}'

# output from remote_2
'{"output": {"avg_beta_vector": [4.816936488169361, -0.7310087173100862, 1.0136986301369817], "r_2_global": 0.9094740875562791, "ts_global": [7.479582268761765, -4.147193188256449, 4.46310566414374], "ps_global": [0.01740954339992219, 0.05351753613331965, 0.04671291787951837], "dof_global": 2}, "success": true}'