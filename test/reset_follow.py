import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mongoengine import connect
connect('PBL6')
from app.models import Follow
from app.models.base.extended_account import ExtendedAccount

for user in ExtendedAccount.objects():
    user.followers_count = 0
    user.following_count = 0
    user.save()
for follow in Follow.objects():
    follow.delete()