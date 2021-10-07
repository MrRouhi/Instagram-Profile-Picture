import instaloader

mod=instaloader.Instaloader()
user=input("Enter Instagram ID : ")

mod.download_profile(user,profile_pic_only=True)