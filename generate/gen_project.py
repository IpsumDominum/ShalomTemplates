import os


def start_template(projectname):
    template = """projectname: {}\nModules:\nModels:
    """.format(projectname)
    return template
def generate_new_project(projectname):
    try:
        os.mkdir(projectname)
        print("~created folder {}".format(projectname))
        os.mkdir(os.path.join(projectname,"build"))
        print("~created folder {}/build".format(projectname))
        os.mkdir(os.path.join(projectname,"models"))
        print("~created folder {}/models".format(projectname))
        with open(os.path.join(projectname,"project.yaml"),'w') as file:
            file.write(start_template(projectname))
        print("~wrote file {}/project.shalom".format(projectname))
    except Exception as e:
        print("ERROR: Unable to initiate project, please check error message:")
        print(e)
        exit()
