def verificationProcess(original_function):

    def normal_function():
        print("Starting of the function")
        original_function()
        print("ENding of the function")

    return normal_function


@verificationProcess
def adminDashboard():
    print("Welcome to the admin dashboard")


# student_dashoard()
# print("-------------------------")
# adminDashboard()


def loginVerification(original_function):

    def verification(user, subscription):
        # user = input("Enter your user (admin/trainer/student) : ")
        # subscription = input("Is subscription paid? (Yes/No)")

        if user == "admin" and subscription == "Yes":

            print(f"{user} dashboard is opened")
            return original_function(user, subscription)

        elif user == "admin" and subscription == "No":
            print("Admin dashboard :  please do subscribt")

    return verification


# @verificationProcess
@loginVerification
def student_dashoard(user, subscritpion):
    print(f"Welcome to the {user} dashboard")


student_dashoard("admin", "No")
