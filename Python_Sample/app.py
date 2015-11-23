from flask import Flask, render_template, request, session
import requests
import json
import config

app = Flask(__name__)
app.config.from_object(config)

# configuration
service_base_url = "https://rest.developer.yodlee.com/services/srest/restserver/v1.0"
cobrand_session_token_url = "/authenticate/coblogin"
user_session_token_url = "/authenticate/login"
search_sites_url = "/jsonsdk/SiteTraversal/searchSite"
get_site_login_form_url = "/jsonsdk/SiteAccountManagement/getSiteLoginForm"
add_site_account_url = "/jsonsdk/SiteAccountManagement/addSiteAccount"
get_item_summaries_url = "/jsonsdk/DataService/getItemSummaries"

# main index
@app.route("/")
def index():
	return render_template("index.html")

# cobrand session token
@app.route("/cobrand-session-token", methods=["GET","POST"])
def cobrand_session_token():
	cobrand_login = request.form.get("cobrand_login")
	cobrand_password = request.form.get("cobrand_password")
	cobrand_session_token = ""
	res_json = ""

	if cobrand_login and cobrand_password:
		uri = service_base_url + cobrand_session_token_url
		payload = {"cobrandPassword": cobrand_password, "cobrandLogin": cobrand_login}
		res = requests.post(uri, params=payload)
		raw = res.json()
		cobrand_session_token = session["cobrand_session_token"] = raw["cobrandConversationCredentials"]["sessionToken"]
		res_json = json.dumps(raw, sort_keys=False, indent=4, separators=(",", ": "))

	return render_template("cobrand-session-token.html", cobrand_session_token=cobrand_session_token, res_json=res_json)

# user session token
@app.route("/user-session-token", methods=["GET","POST"])
def usersessiontoken():
	user_login = request.form.get("user_login")
	user_password = request.form.get("user_password")
	user_session_token = ""
	res_json = ""

	if user_login and user_password:
		cobrand_session_token = session["cobrand_session_token"]
		uri = service_base_url + user_session_token_url
		payload = {"cobSessionToken": cobrand_session_token, "password": user_password, "login": user_login}
		res = requests.post(uri, params=payload)
		raw = res.json()
		user_session_token = session["user_session_token"] = raw["userContext"]["conversationCredentials"]["sessionToken"]
		session["user_context"] = raw["userContext"]
		res_json = json.dumps(raw, sort_keys=False, indent=4, separators=(",", ": "))

	return render_template("user-session-token.html", user_session_token=user_session_token, res_json=res_json)

# search sites
@app.route("/search-sites", methods=["GET","POST"])
def searchsites():
	cobrand_session_token = session["cobrand_session_token"]
	user_session_token = session["user_session_token"]
	site_string_search = request.form.get("site_string_search")
	res_json = ""

	if cobrand_session_token and user_session_token and site_string_search:
		uri = service_base_url + search_sites_url
		payload = {"siteSearchString": site_string_search, "userSessionToken": user_session_token, "cobSessionToken": cobrand_session_token}
		res = requests.post(uri, params=payload)
		raw = res.json()
		res_json = json.dumps(raw, sort_keys=False, indent=4, separators=(",", ": "))
		parsed_json = json.loads(res_json)
		session["site_id"] = parsed_json[0]["siteId"]

	return render_template("search-sites.html", cobrand_session_token=cobrand_session_token, user_session_token=user_session_token, res_json=res_json)

# site login form
@app.route("/site-login", methods=["GET","POST"])
def sitelogin():
	cobrand_session_token = session["cobrand_session_token"]
	user_session_token = session["user_session_token"]
	site_id = "16441"
	res_json = ""

	if cobrand_session_token and user_session_token and site_id:
		uri = service_base_url + get_site_login_form_url
		payload = {"siteId": site_id, "userSessionToken": user_session_token, "cobSessionToken": cobrand_session_token}
		res = requests.post(uri, params=payload)
		raw = res.json()
		res_json = json.dumps(raw, sort_keys=False, indent=4, separators=(",", ": "))

	return render_template("site-login.html", cobrand_session_token=cobrand_session_token, user_session_token=user_session_token, site_id=site_id, res_json=res_json)

# site account management
@app.route("/site-account", methods=["GET","POST"])
def siteaccount():
	cobrand_session_token = session["cobrand_session_token"]
	user_session_token = session["user_session_token"]
	site_id = "16441"
	user_login = request.form.get("credentialFields[0].value")
	user_password = request.form.get("credentialFields[1].value")
	res_json = ""

	if user_login and user_password:
		uri = service_base_url + add_site_account_url
		payload = {"credentialFields[1].value": user_password, "credentialFields[0].value": user_login, "siteId": site_id, "userSessionToken": user_session_token, "cobSessionToken": cobrand_session_token}
		res = requests.post(uri, params=payload)
		raw = res.json()
		res_json = json.dumps(raw, sort_keys=False, indent=4, separators=(",", ": "))

	return render_template("site-account.html", \
		cobrand_session_token=cobrand_session_token, user_session_token=user_session_token, site_id=site_id, res_json=res_json)

# item summaries
@app.route("/item-summaries", methods=["GET","POST"])
def itemsummaries():
	cobrand_session_token = session["cobrand_session_token"]
	user_session_token = session["user_session_token"]
	res_json = ""

	if cobrand_session_token and user_session_token:
		cobrand_session_token = session["cobrand_session_token"]
		user_session_token = session["user_session_token"]
		payload = {"userSessionToken": user_session_token, "cobSessionToken": cobrand_session_token}
		uri = service_base_url + get_item_summaries_url
		res = requests.post(uri, params=payload)
		raw = res.json()
		res_json = json.dumps(raw, sort_keys=False, indent=4, separators=(",", ": "))

	return render_template("item-summaries.html", cobrand_session_token=cobrand_session_token, user_session_token=user_session_token, res_json=res_json)


if __name__ == "__main__":
	app.run(debug=True)