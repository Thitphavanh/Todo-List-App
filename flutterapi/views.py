from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TodolistSerializer
from .models import Todolist

# GET Data
@api_view(['GET'])
def all_todolist(request):
    alltodolist = Todolist.objects.all() # ດຶງຂໍ້ມູນຈາກ model Todolist
    serializer = TodolistSerializer(alltodolist,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# POST Data (save data to database)
@api_view(['POST'])
def post_todolist(request):
    if request.method == 'POST':
        serializer = TodolistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
            
@api_view(['PUT'])
def update_todolist(request,TID):
    # localhost:8000/api/update-todolist/13
    todo = Todolist.objects.get(id=TID)
    if request.method == 'PUT':
        data = {}
        serializer = TodolistSerializer(todo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['status'] = 'updated'
            return Response(data=data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        

@api_view(['DELETE'])
def delete_todolist(request,TID):
    todo = Todolist.objects.get(id=TID)

    if request.method == 'DELETE':
        delete = todo.delete()
        data = {}
        if delete:
            data['status'] = 'deleted'
            statuscode = status.HTTP_200_OK
        else:
            data['status'] = 'failed'
            statuscode = status.HTTP_400_BAD_REQUEST

        return Response(data=data, status=statuscode)


data = [
    {
        "title": "ເຈາະລຶກກ່ຽວກັບປັນຍາປະດິດ!",
        "subtitle": "AI ຍໍ່ມາຈາກ Artificial Intelligence ແປເປັນລາວ ແມ່ນ ປັນຍາປະດິດ ເປັນລະດັບຊັ້ນໜຶ່ງໃນວິທະຍາສາດຄອມພິວເຕີຣ໌",
        "image_url": "https://raw.githubusercontent.com/Thitphavanh/BasicAPI/main/AI.jpg",
        "detail": "AI ນັ້ນຖືກພັດທະນາມາໃຫ້ໃຊ້ງານແທນຄົນຕົວຢ່າງລະບົບຄໍລເຊັນເຕີຣ໌ຕ່າງໆ ເພື່ອຫຼຸດການໃຊ້ແຮງງານຄົນ ແລະ ສ້າງຄວາມເພິ່ງພໍໃຈໃຫ້ກັບລູກຄ້າ ຄາດການວ່າໃນອະນາຄົດ AI ຈະສາມາດເຮັດວຽກແທນຄົນໃນສິ່ງທີ່ສະຫຼັບຊັບຊ້ອນເຊັ່ນ: ການວາງແຜນ, ວາງກົນລະຍຸດທາງການຕະຫຼາດ ລວມເຖິງການພິຈາລະນາເນື້ອໃນໃຈຄວາມຕ່າງໆ ສະນັ້ນຫາກທ່ານບໍ່ຢາກເປັນຄົນຕົກຍຸກກໍ່ຕ້ອງໄດ້ຮຽນຮູ້ມັນໄວ້ ເພາະມີຄວາມສຳຄັນຫຼາຍຕໍ່ທຸລະກິດຂອງທ່ານໃນພາຍໜ້າ\n\nAI ແມ່ນວິທີການເຮັດໃຫ້ຄອມພີວເຕີຣ໌ມີຄວາມສາມາດຄ້າຍຄືມະນຸດ ເຊິ່ງຫຍໍ້ມາຈາກ ຄຳວ່າ Artificial Intelligence ຫຼື ເອີ້ນວ່າປັນຍາປະດິດ ເປັນຂະແໜງວິທະຍາສາດໜຶ່ງຂອງຄອມພີວເຕີຣ໌ທີ່ກ່ຽວກັບວິທີການເຮັດໃຫ້ຄອມພີວເຕີຣ໌ມີສາມາດຄ້າຍຄືມະນຸດ ຫຼື ຮຽນແບບພືດຕິກຳຂອງມະນຸດຄືກັບໂປຣແກມຊອຟຕ໌ແວຣ໌ຕ່າງໆທີ່ໃຊ້ກັບຄອມພີວເຕີຣ໌"
    },
    {
        "title": "ເທຄໂນໂລຢີສຳຄັນແນວໃດ?",
        "subtitle": "ເທຄໂນໂລຢີມີຄວາມສຳຄັນຫຼາຍຕໍ່ກັບໂລກຂອງເຮົາໃນອານາຄົດ",
        "image_url": "https://raw.githubusercontent.com/Thitphavanh/BasicAPI/main/Technology.jpg",
        "detail": "ເທຄໂນໂລຢີ (Technology) ແມ່ນ ການໃຊ້ຄວາມຮູ້ ເຄື່ອງມື ຄວາມຄິດ ຫຼັກການ ເທຄນິຄ ຄວາມຮູ້ ລະບຽບວິທີ ກະບວນການຕະຫຼອດຈົນ ຜົນງານທາງວິທະຍາສາດທັ້ງສິ່ງປະດິດ ແລະ ວິທິການ\n\nມາປະຍຸກໃຊ້ໃນລະບົບວຽກເພື່ອຊ່ວຍໃຫ້ເກີດການປ່ຽນແປງໃນການເຮັດວຽກໃຫ້ດີຍິ່ງຂຶ້ນ ແລະ ເພື່ອເພີ່ມປສິດທິພາບ ແລະ ປະສິດທິຜົນຂອງງານໃຫ້ມີຫຼາຍຍິ່ງຂຶ້ນ"
    },
    {
        "title": "ອິນເຕີຣ໌ເນັຕຂອງສິ່ງຕ່າງໆ?",
        "subtitle": "IoT (Internet of Things) ປະກາດກຽດຕິຄຸນຈາກຜູ້ປະກອບການ Kevin Ashton ໜຶ່ງໃນຜູ້ກໍ່ຕັ້ງ Auto-ID Center ຂອງ MIT",
        "image_url": "https://raw.githubusercontent.com/Thitphavanh/BasicAPI/main/IoT.jpg",
        "detail": "Internet of Things (IoT) ແມ່ນ Internet of Things (IoT) ແມ່ນ ການທີ່ອຸປະກອນອິເລັກທໍຣນິກສ໌ຕ່າງໆ ສາມາດເຊື່ອມໂຢງ ຫຼື ສົ່ງຂໍ້ມູນເຖິງກັນໄດ້ດ້ວຍອິນເຕີຣ໌ເນັຕ ໂດຍບໍ່ຕ້ອງປ້ອນຂໍ້ມູນ ການເຊື່ອມໂຢງນີ້ງ່າຍຈົນເຮັດໃຫ້ເຮົາສາມາດສັ່ງການຄວບຄຸມການໃຊ້ງານອຸປະກອນອິເລັກທໍຣນິກສ໌ຕ່າງໆ\n\nຜ່ານທາງເຄືອຂ່າຍອິນເຕີຣ໌ເນັຕໄດ້ ໄປຈົນເຖິງການເຊື່ອມໂຢງການໃຊ້ງານອຸປະກອນອິເລັກທໍຣນິກສ໌ຕ່າງໆ ຜ່ານທາງເຄືອຂ່າຍອິນເຕີຣ໌ເນັຕເຂົ້າກັບການໃຊ້ງານອື່ນໆ ຈົນເກີດເປັນບັນດາ Smart ຕ່າງໆ\n\nໄດ້ແກ່ Smart Device, Smart Grid, Smart Home, Smart Network, Smart Intelligent Transportation ທັງຫຼາຍທີ່ເຮົາເຄີຍໄດ້ຍິນນັ້ນເອງ ຊຶ່ງແຕກຕ່າງຈາກໃນອາດີດທີ່ອຸປະກອນອິເລັກທໍຣນິກສ໌ເປັນພຽງສື່ກາງໃນການສົ່ງ ແລະ ສະແດງຂໍ້ມູນເທົ່ານັ້ນ"
    },
    {
        "title": "ຫຸ້ນແມ່ນຫຍັງ?",
        "subtitle": "ຫຸ້ນແມ່ນສິດຄວາມເປັນເຈົ້າຂອງໃນກິດຈະການ ຫຼື ບໍລິສັດ",
        "image_url": "https://raw.githubusercontent.com/Thitphavanh/BasicAPI/main/Stock.jpg",
        "detail": "ຫຸ້ນ ແມ່ນຫຸ້ນສ່ວນທາງດ້ານເສດຖະກິດ, ດ້ານການລົງທືນຜູ້ຮ່ວມລົງທືນເພື່ອໃຫ້ໄດ້ຜົນກຳໄລນຳກັນ. \n\nເວົ້າງ່າຍໆ ທຸກຄົນທີ່ມີຫຸ້ນຂອງບໍ່ລິສັດໃດຫນື່ງກໍ່ຫມາຍຄວາມວ່າຜູ້ນັ້ນກໍ່ເປັນເຈົ້າຂອງທຸລະກິດ, ມີສິດແລະໄດ້ເງີນປັນຜົນກັບບໍ່ລິສັດນັ້ນເຊັ່ນກັນ ແຕ່ຈະມີສິດແລະໄດ້ເງີນປັນຜົນຫນ້ອຍຫລືຫລາຍນັ້ນ ມັນກໍ່ຂື່ນຢູ່ກັບບຸກຄົນນັ້ນຈະມີຫຸ້ນຫນ້ອຍຫລືຫລາຍສຳໃດຢູ່ໃນບໍລິສັດນັ້ນ"
    },
    {
        "title": "ຄວາມຮູ້ກ່ຽວກັບຄຣິປໂຕເຄີຣ໌ເຣນຊີ!",
        "subtitle": "ສະກຸນເງິນດິຈິທັລຄຣິປໂຕເຄີຣ໌ເຣນຊີທຸກຊະນິດບໍ່ໄດ້ຖືກກຳນົດ ຫຼື ຄວບຄຸມຜ່ານໜ່ວຍງານທາງການເງິນສາກົນໃດໆ",
        "image_url": "https://raw.githubusercontent.com/Thitphavanh/BasicAPI/main/cryptocurrency.jpg",
        "detail": "Cryptocurrency (ສະກຸນເງິນດິຈິທັລ) ແມ່ນ ສິນຊັບດິຈິທັລປະເພດໜຶ່ງທີ່ມີການເຂົ້າລະຫັດ ມີລາຄາກາງໃນການຊື້ຂາຍແປຜັນຕາມກົດໄກຕະຫຼາດ ຈຶ່ງສາມາດເຮັດໜ້າທີ່ເປັນສື່ກາງໃນການແລກປ່ຽນມູນຄ່າຜ່ານອິນເທີຣ໌ເນັດໄດ້\n\nແຕ່ເພາະບໍ່ໄດ້ມີລັກສະນະທາງກາຍຍະພາບຄືກັບສະກຸນເງິນທົ່ວໄປ (Fiat Currency) ຂອງແຕ່ລະປະເພດທີ່ມີການຕີພິມພັນທະບັນອອກມາ ເຮັດໃຫ້ບາງຄັ້ງເຮົາກໍ່ເອີ່ນ ສະກຸນເງິນດິຈິທັລ ວ່າ ສະກຸນເງິນຄືເງິນແທ້ ຫຼື Virtual currency"
    },
    {
        "title": "ພະລັງງານໄຟຟ້າແຫ່ງອານາຄົດເປັນແນວ?",
        "subtitle": "ແມ່ນ ພະລັງງານທາງເລືອກ ໃນໂລກອານາຄົດອັນໃກ້",
        "image_url": "https://raw.githubusercontent.com/Thitphavanh/BasicAPI/main/Energy.jpg",
        "detail": "ບາງຄົນຍັງຄາດຄະເນວ່າພະລັງງານດັ່ງກ່າວໃນອະນາຄົດອັນໃກ້ນີ້ຈະທົດແທນຖ່ານຫີນ, ອາຍແກັສ, ໂຮງງານໄຟຟ້ານິວເຄຼຍ. ຫນຶ່ງໃນເຂດຂອງພະລັງງານສີຂຽວແມ່ນພະລັງງານລົມ. ເຄື່ອງກໍາເນີດໄຟຟ້າທີ່ປ່ຽນພະລັງງານລົມເປັນໄຟຟ້າແມ່ນບໍ່ພຽງແຕ່ອຸດສາຫະກໍາ, ເປັນສ່ວນຫນຶ່ງຂອງການກະສິກໍາລົມ, ແຕ່ຍັງມີຂະຫນາດນ້ອຍ, ການບໍລິການກະສິກໍາສ່ວນຕົວ"
    }
]

def Home(request):
    return JsonResponse(data=data,safe=False,json_dumps_params={'ensure_ascii':False})
