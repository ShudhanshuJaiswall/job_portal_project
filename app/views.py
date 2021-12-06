from django.core.checks import messages
from django.db.models import expressions
from django.shortcuts import redirect, render,HttpResponse
from django.http import request
from .models import * 
from random import randint
# Create your views here.
def IndexPage(request):
    return render(request,'app/base1.html')
def SignupPage(request):
    return render(request,'app/signup.html')

def RegisterUser(request):
    if request.POST['role']=="Candidate":
        role = request.POST['role']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
         
        user = UserMaster.objects.filter(email=email)
            #server side validation
        if user: 
            message="User Already Exits"
            return render(request,"app/signup.html",{'msg':message})
        else:
            if password ==cpassword:
                otp=randint(10000,99999)
                newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                newcand = Candidate.objects.create(user_id=newuser,firstname=fname,lastname=lname)
                return render(request,"app/otpvarify.html",{'email':email})
                
    else:
        #print("Company Registration")
        if request.POST['role']=="Company":
            role = request.POST['role']
            fname = request.POST['firstname']
            lname = request.POST['lastname']
            email = request.POST['email']
            password = request.POST['password']
            cpassword = request.POST['cpassword']
                        
            user = UserMaster.objects.filter(email=email)
                #server side validation
            
            if user:
                message="Company Already Exits"
                return render(request,"app/signup.html",{'msg':message})
            
            else:
                if password ==cpassword:
                    otp=randint(10000,99999)
                    newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                    newcompany = Company.objects.create(user_id=newuser,firstname=fname,lastname=lname)
                    return render(request,"app/otpvarify.html",{'email':email})
def Loginpage(request):
    return render(request,"app/login.html")

def LoginUser(request):
    if request.POST['role']=="Candidate":
        email=request.POST['email']
        password=request.POST['password']
        user = UserMaster.objects.get(email=email)
        if user:
            if user.password==password and user.role=="Candidate":
                can = Candidate.objects.get(user_id=user)
                request.session['id']= user.id
                request.session['role']=user.role
                request.session['firstname']=can.firstname
                request.session['lastname']=can.lastname
                request.session['email']=user.email
                return redirect('myaccount')
            else:
                message ="Password does not match"
                return render(request,"app/login.html",{'msg':message})
        else:
            message ="User doesnot exit"
            return render(request,"app/login.html",{'msg':message})  
    else:
        if request.POST['role']=="Company":
            email=request.POST['email']
            password=request.POST['password']
            user=UserMaster.objects.get(email=email)
            if user:
                if user.password==password and user.role=='Company':
                    can=Company.objects.get(user_id=user)   
                    request.session['id'] = user.id
                    request.session['role'] = user.role
                    request.session['firstname'] = can.firstname
                    request.session['lastname'] = can.lastname
                    request.session['email'] = user.email
                    return render(request,"app/company/index.html")
                else:
                    message ="Password does not match"
                    return render(request,"app/login.html",{'msg':message})
            else:
               message ="Company doesnot exit"
               return render(request,"app/login.html",{'msg':message}) 
def OTPPage(request):
    return render(request,"app/otpvarify.html")

def Otpvarify(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])

    user = UserMaster.objects.get(email=email)
    if user:
        if user.otp == otp:
            message ="Otp Verify Successfully"
            return render(request,"app/login.html",{'msg':message})
        else:
            message = "OTP is incorrect Retry "
            return render(request,"app/otpvarify.html",{'msg':message})
    else:
        return render(request,"app/signup.html")
def ProfilePage(request,pk):
        user = UserMaster.objects.get(pk=pk)
        can =Candidate.objects.get(user_id=user)
        return render(request,"app/profile.html",{'user':user,'can':can})

def UpdateProfile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Candidate":
        can = Candidate.objects.get(user_id=user)
        can.country = request.POST['country']
        can.state =request.POST['state']#first state for database field amd second from form
        can.city =request.POST['city']
        can.contact =request.POST['contact']
        can.gender =request.POST['gender']
        can.dob =request.POST['dob']
        can.profile_pic =request.POST['image']
        can.save()
        url = f'/profile/{pk}'  #formating URL
        return redirect(url)

def Browse(request):
    return render(request,"app/browse-jobs.html")
    
def PostJob(request):
    return render(request,"app/post-job.html")

def About(request):
    return render(request,"app/about.html")

def Home1(request):
    return render(request,"app/home1.html")

def JobPage(request):
    return render(request,"app/job-page.html")

def JobDetail(request):
    return render(request,"app/job-details.html")

def Resume(request):
    return render(request,"app/resume.html")

def Privacy(request):
    return render(request,"app/privacy-policy.html")

def FAQ(request):
    return render(request,"app/faq.html")

def Pricing(request):
    return render(request,"app/pricing.html")

def Contact(request):
    return render(request,"app/contact.html")

def BrowseJob(request):
    return render(request,"app/browse-jobs.html")

def BrowseCat(request):
    return render(request,"app/browse-categories.html")

def AddResume(request):
    return render(request,"app/add-resume.html")

def ManageResume(request):
    return render(request,"app/manage-resumes.html")

def JobAlert(request):
    return render(request,"app/job-alerts.html")

def PostJob(request):
    return render(request,"app/post-job.html")

def ManageJob(request):
    return render(request,"app/manage-jobs.html")

def ManageAppli(request):
    return render(request,"app/manage-applications.html")

def BrowseResume(request):
    return render(request,"app/browse-resumes.html")

def Blog(request):
    return render(request,"app/blog.html")

def BlogSlider(request):
    return render(request,"app/blog-left-sidebar.html")

def BlogFull(request):
    return render(request,"app/blog-full-width.html")

def SinglePost(request):
    return render(request,"app/single-post.html")

def MyAccount(request):
    return render(request,"app/my-account.html")

def ApplyPage(request,pk):
     user = request.session['id']
     if user:
         cand = Candidate.objects.get(user_id=user)
         job = JobDettails.objects.get(id=pk)
     return render(request,"app/apply.html",{'user':user,'cand':cand,'job':job})

def ApplyJob(request,pk):
    user=request.session['id']
    if user:
        can = Candidate.objects.get(user_id= user)
        job =JobDettails.objects.get(id=pk)
        edu = request.POST['education']
        exp = request.POST['experience']
        web = request.POST['website']
        min_salary=request.POST['minsalary']
        max_salary=request.POST['maxsalary']
        gender = request.POST['gender']
        resume = request.FILES['resume']
        newapply = ApplyJob.objects.create(candidate=can,job=job,education=edu,experience=exp,website=web,min_salary=min_salary
        ,max_salary=max_salary,gender=gender,resume=resume)
        message ="Apply Successfully"
        return render(request,"app/apply.html",{'msg':message})
#@@@@@@@@@@@@@@@@@@@@@@@@@   Company Side       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def ComapnyIndex(request):
    return render(request,"app/company/index.html")

def Companyregister(request):
    return render(request,"app/company/register.html")

def Companylogin(request):
    return render(request,"app/company/login.html")

def Companyprofile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    comp = Candidate.objects.get(user_id=user)
    return render(request,"app/company/profile.html",{'user':user,'comp':comp})

def Updateprofile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Company":
        comp=Candidate.objects.get(user_id=user)
        comp.firstname=request.POST['firstname']
        comp.lastname=request.POST['lastname']
        comp.company_name=request.POST['companyname']
        comp.state=request.POST['state']
        comp.website=request.POST['website']
        comp.address=request.POST['address']
        comp.city=request.POST['city']
        comp.save()
        url = f"/companyprofile/{pk}"
        return redirect(url)
def Jobpost(request):
    return render(request,"app/company/jobpost.html")

def JobDetailSubmit(request,pk):
    user=UserMaster.objects.get(pk=pk)
    if user.role=="Company":
        comp=Company.objects.get(user_id=user)
        jobname=request.POST['jobname']
        companyname=request.POST['cname']
        companyemail=request.POST['email']
        companycontact=request.POST['ccontact']
        address=request.POST['address']
        jobdescriptions=request.POST['jobdescriptions']
        qualifications=request.POST['qualifications']
        responsebility=request.POST['responsibility']
        location=request.POST['location']
        salary=request.POST['salary']
        exprerience=request.POST['experience']
        website=request.POST['cwebsite']
        logo=request.FILES['image']

        newjob=JobDettails.objects.create(company_id=comp,jobname=jobname,companyname=companyname,companycontact=companycontact,
        companyaddress=address,jobdescription=jobdescriptions,qualification=qualifications,responsiblity=responsebility,
        location=location,companyemail=companyemail,salarypackage=salary,experience=exprerience,companywebsite=website,logo=logo)

        message="Job Post Suceessfully"
        return render(request,"app/company/jobpost.html",{'msg':message})

def JobPageList(request):
    all_job=JobDettails.objects.all()
    return render(request,"app/company/postjoblist.html",{'all_job':all_job})

def CnadidateJobPageList(request):
    all_job=JobDettails.objects.all()
    return render(request,"app/browse-jobs.html",{'all_job':all_job})

def ApplyList(request):
    all_jobapply= ApplyJob.objects.all()
    return render(request,"app/company/applyjoblist.html",{'all_job':all_jobapply})

def Companylogout(request):
    del request.session['email']
    del request.session['password']
    return redirect('base1')

############################## ADMIN SIDE @@@@@@@@@@@@###########################!!!!!!!!!!!!!!!!!
def AdminLoginPage(request):
    return render(request,"app/admin/login.html")

def AdminIndexPage(request):
    if 'username' in request.session and 'password' in request.session:
        return render(request,"app/admin/index.html")
    else:
        return redirect('adminloginpage')
def AdminLogin(request):
    username = request.POST['username']
    password = request.POST['password']

    if username=="admin" and password=="admin":
        request.session['username'] = username
        request.session['password'] = password
        return redirect('adminindexpage')
    else:
        message ="Username and password not match"
        return render(request,"app/admin/login.html",{'msg':message})
def AdminUserList(request):
    all_user=UserMaster.objects.filter(role="Candidate")
    return render(request,"app/admin/userlist.html",{'alluser':all_user})

def AdminCompanyList(request):
    all_company=UserMaster.objects.filter(role="Company")
    return render(request,"app/admin/companylist.html",{'allcompany':all_company})

def UserDelete(redirect,pk):
    user = UserMaster.objects.get(pk=pk)
    user.delete()
    return redirect('userlist')

def VerifyCompanyPage(request,pk):
    company = UserMaster.objects.get(pk=pk)
    if company:
        return render(request,"app/admin/verify.html",{'company':company})

def VerifyCompany(request,pk):
    company=UserMaster.objects.get(pk=pk)
    if company:
        company.is_verified=request.POST['verify']
        company.save()
        return redirect('companylist')
def CompanyDelete(redirect,pk):
    company=UserMaster.objects.get(pk=pk)
    company.delete()
    return redirect('companylist')
