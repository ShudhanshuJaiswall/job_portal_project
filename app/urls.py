from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.IndexPage,name="index"),
    path("signup/",views.SignupPage,name="signup"),
    path("register/",views.RegisterUser,name="register"),
    path("otppage/",views.OTPPage,name="otppage"),
    path("otp/",views.Otpvarify,name="otp"),
    path("loginpage/",views.Loginpage,name="loginpage"),
    path("loginuser/",views.LoginUser,name="login"),
    path("profile/<int:pk>",views.ProfilePage,name="profile"),
    path("updateprofile/<int:pk>",views.UpdateProfile,name="updateprofile"),
    path("browse/",views.Browse,name="browse"),
    path("postjob/",views.PostJob,name="postjob"),
    path("about/",views.About,name="about"),
    path("home1/",views.Home1,name="home1"),
    path("jobpage/",views.JobPage,name="jobpage"),
    path("jobdetail/",views.JobDetail,name="jobdetail"),
    path("resume/",views.JobDetail,name="resume"),
    path("privacy/",views.Privacy,name="privacy"),
    path("frequency/",views.FAQ,name="faq"),
    path("pricing/",views.Pricing,name="pricing"),
    path("contact/",views.Contact,name="contact"),
    path("Browsecat/",views.BrowseCat,name="browsecat"),
    path("addresume/",views.AddResume,name="addresume"),
    path("manageresume/",views.ManageResume,name="manageresume"),
    path("jobalert/",views.JobAlert,name="jobalerts"),
    path("Postjob/",views.PostJob,name="post-job"),
    path("Managejob/",views.ManageJob,name="manage-job"),
    path("Manageapplications/",views.ManageAppli,name="manage-appli"),
    path("Myaccount/",views.MyAccount,name="myaccount"),
    path("BrowseResume/",views.BrowseResume,name="browse-resumes"),
    path("Blog/",views.Blog,name="blog"),
    path("Blogsidebar/",views.BlogSlider,name="blog-slider"),
    path("Blogfull/",views.BlogFull,name="blogfull"),
    path("singlepost/",views.SinglePost,name="singlepost"),
    path("candidatejoblist/",views.CnadidateJobPageList,name="candidatejoblist"),
    path("applyjob/<int:pk>",views.ApplyPage,name="applyjob"),
    path("apply/<int:pk>",views.ApplyJob,name="apply"),
#############################Company URL@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    path("company/",views.ComapnyIndex,name="companyindex"),
    path("companyregister/",views.Companyregister,name="companyregister"),
    path("companylogin/",views.Companylogin,name="companylogin"),
    path("companyprofile/<int:pk>",views.Companyprofile,name="companyprofile"),
    path("updatecompanyprofile/<int:pk>",views.UpdateProfile,name="updatecompanyprofile"),
    path("jobpostpage/",views.Jobpost,name="jobpostpage"),
    path("jobpost/<int:pk>",views.JobDetailSubmit,name="jobpost"),
    path("joblisttable/",views.JobPageList,name="joblisttable"),
    path("companylogout/",views.Companylogout,name="companylogout"),

    #############################          Admin Side       *************************


    path("adminloginpage/",views.AdminLoginPage,name="adminloginpage"),
    path("adminindexpage/",views.AdminIndexPage,name="adminindexpage"),
    path("adminlogin/",views.AdminLogin,name="adminlogin"),
    path("adminuserlist/",views.AdminUserList,name="userlist"),
    path("admincompanylist/",views.AdminCompanyList,name="companylist"),
    path("userdelete/<int:pk>",views.UserDelete,name="userdelete"),
    path("companyverify/<int:pk>",views.VerifyCompanyPage,name="companyverify"),
    path("verifycompany/<int:pk>",views.VerifyCompany,name="verify"),
    path("companydelete/<int:pk>",views.CompanyDelete,name="companydelete"),
]
