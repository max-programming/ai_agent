from functions.get_files_info import get_files_info


def main():
    working_dir = "calculator"
    root_contents = get_files_info(working_dir)
    print(root_contents)
    pkg_contents = get_files_info(working_dir, "pkg")
    print(pkg_contents)
    bin_contents = get_files_info(working_dir, "bin")
    print(bin_contents)
    back_directory = get_files_info(working_dir, "../")
    print(back_directory)


main()
