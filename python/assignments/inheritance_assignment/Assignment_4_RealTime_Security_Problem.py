print("--5-Real-Time Security Platform Example----")
class SecurityUser:

    def security_login(self):
        print("Security user logged in")

    def view_alerts(self):
        print("Viewing security alerts")


class CloudSecurityUser(SecurityUser):

    def connect_cloud(self):
        print("Connected to cloud")

    def scan_resources(self):
        print("Scanning cloud resources")


class CloudSecurityAdmin(CloudSecurityUser):

    def manage_users(self):
        print("Managing security users")

    def block_threat(self):
        print("Blocking security threat")


admin = CloudSecurityAdmin()

admin.security_login()
admin.view_alerts()    

admin.connect_cloud()  
admin.scan_resources()

admin.manage_users()
admin.block_threat()