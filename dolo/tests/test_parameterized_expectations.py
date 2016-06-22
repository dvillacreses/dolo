def test_parameterized_expectations_direct():

    from dolo import yaml_import
    from dolo.algos.dtcscc.parameterized_expectations import  parameterized_expectations_direct
    from dolo.algos.dtcscc.time_iteration import time_iteration_direct

    model = yaml_import("examples/models/rbc_full.yaml")

    dr_ti = time_iteration_direct(model)
    dr_pea = parameterized_expectations_direct(model)

    x_ti  = dr_ti(dr_ti.grid)
    x_pea = dr_pea(dr_ti.grid)

    print(abs(x_ti - x_pea).max()<1e-5)


if __name__ =='__main__':
    test_parameterized_expectations_direct()
