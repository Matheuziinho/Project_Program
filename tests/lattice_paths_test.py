from project_program.lattice_paths import lattice_paths


def test_lattice_paths() -> None:
    assert lattice_paths(2, 2) == 6, "Should be 6"
    assert lattice_paths(3, 3) == 20, "Should be 20"
    assert lattice_paths(20, 20) == 137_846_528_820, "Should be 137_846_528_820"
