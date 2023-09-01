# Spinny-Keshav-Allawadi
Deployed URL : https://heykeshav.pythonanywhere.com
<br/>
<pre>
ADMIN:   https://heykeshav.pythonanywhere.com/admin/
Username : keshav
Password : keshav
</pre>
<br/>
<pre>
Staff:   https://heykeshav.pythonanywhere.com/api-auth/login
Username : user1
Password : user1
</pre>
<br/>
<pre>
Endpoints:

prefix : https://heykeshav.pythonanywhere.com/store/
<br/>
suffix :
register/		- (POST) User registration
login/			- (POST) Staff memeber can login to get token
box/create/		- (POST) Registered staff can create a box
box/all-box/		- (GET) Any user can can get list of box without createdBy and updatedOn
box/user-box/		- (GET) A Staff member can get details of their created box with all details
box/update/{id}		- (PUT) Any registered staff can update the box excluding createdBy and createdOn field
box/delete/{id}		- (DELETE) Only the Box owner can delete their box
</pre>
