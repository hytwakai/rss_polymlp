import argparse


class ParseArgument:
    @classmethod
    def get_initial_structure_args(cls):
        parser = argparse.ArgumentParser()
        cls._add_initial_structure_arguments(parser)
        args = parser.parse_args()
        return args

    @classmethod
    def get_optimization_args(cls):
        parser = argparse.ArgumentParser()
        cls._add_optimization_arguments(parser)
        return parser.parse_args()

    @classmethod
    def get_parallelization_args(cls):
        parser = argparse.ArgumentParser()
        cls._add_optimization_arguments(parser)
        cls._add_parallelization_arguments(parser)
        return parser.parse_args()

    @staticmethod
    def _add_initial_structure_arguments(parser):
        # Settings in generating initial structures
        parser.add_argument(
            "--elements",
            type=str,
            nargs="+",
            default=None,
            help="List of element symbols",
        )
        parser.add_argument(
            "--atom_counts",
            type=int,
            nargs="+",
            default=None,
            help="Number of atoms for each element",
        )
        parser.add_argument(
            "--num_init_str",
            type=int,
            default=5000,
            help="Number of randomly generated initial structures",
        )
        parser.add_argument(
            "--least_distance",
            type=float,
            default=0.0,
            help="Minimum interatomic distance in initial structure (angstrom)",
        )
        parser.add_argument(
            "--max_volume",
            type=float,
            default=100.0,
            help="Maximum volume of initial structure (A^3/atom)",
        )
        parser.add_argument(
            "--min_volume",
            type=float,
            default=0.0,
            help="Minimum volume of initial structure (A^3/atom)",
        )

    @staticmethod
    def _add_optimization_arguments(parser):
        # Settings in geometry optimizations
        parser.add_argument(
            "--pot",
            nargs="*",
            type=str,
            default="polymlp.yaml",
            help="Potential file for polynomial MLP",
        )
        parser.add_argument(
            "--num_opt_str",
            type=int,
            default=1000,
            help="Maximum number of optimized structures obtained from RSS",
        )
        parser.add_argument(
            "--pressure", type=float, default=0.0, help="Pressure term (in GPa)"
        )
        parser.add_argument(
            "--solver_method", type=str, default="CG", help="Type of solver"
        )
        parser.add_argument(
            "--maxiter",
            type=int,
            default=100,
            help="Maximum number of iterations when c1 and c2 values are changed",
        )
        parser.add_argument(
            "--first_poscar",
            type=int,
            default=0,
            help="Index of the POSCAR to be used for the first geometry optimization "
            "in srun parallelization method.",
        )

    @staticmethod
    def _add_parallelization_arguments(parser):
        # Settings for parallelization
        parser.add_argument(
            "--parallel_method",
            type=str,
            choices=["joblib", "srun"],
            default="joblib",
            help="Select parallelization method: 'joblib' or 'srun'.",
        )
        parser.add_argument(
            "--num_process",
            type=int,
            default=-1,
            help="Number of processes to use with joblib. Use -1 to use all available CPU cores.",
        )
        parser.add_argument(
            "--backend",
            type=str,
            choices=["loky", "threading", "multiprocessing"],
            default="loky",
            help="Backend for joblib parallelization",
        )
