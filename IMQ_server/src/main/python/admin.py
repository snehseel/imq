from admin_string_literal import Admin_string_literal
from admin_operations import Admin_operations
from db.db_con import Db_con

class Admin:
    def call_admin_operation(self, argument):
        self.db_con = Db_con.connect_to_db()
        if argument == 1:
            Admin_operations.create_topic(self, self.db_con)
        elif argument == 2:
            Admin_operations.remove_topic(self, self.db_con)
        elif argument == 3:
            Admin_operations.restrict_topic(self, self.db_con)
        elif argument == 4:
            Admin_operations.purge_topic(self, self.db_con)
        elif argument == 5:
            Admin_operations.edit_message(self, self.db_con)
        elif argument == 6:
            Admin_operations.delete_message(self, self.db_con)
        elif argument == 7:
            Admin_operations.show_subscribers(self, self.db_con)
        elif argument == 8:
            Admin_operations.show_publishers(self, self.db_con)
        else:
            print("Invalid choice")

if __name__ == "__main__":
    admin = Admin()
    operation = int(input(Admin_string_literal.admin_menu_string))
    admin.call_admin_operation(operation)
