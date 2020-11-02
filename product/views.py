from django.shortcuts import render
import cx_Oracle

# Create your views here.


def products(request):
    return render(request, 'product/products.html')


def list(request, id):
    dict_result = []
    dsn_tns  = cx_Oracle.makedsn('localhost','1521',service_name='ORCL')
    conn = cx_Oracle.connect(user='bikroy',password='bikroy',dsn=dsn_tns)
   # print(id)
    if id == 1:
        cursor = conn.cursor()
        sql = "SELECT p.PRODUCT_NAME,d.DEVICE_CATAGORY,price,CONDITION, p.product_id FROM product p,DEVICES d,ADVERTISEMENT ad WHERE d.PRODUCT_ID=p.PRODUCT_ID and ad.ADVERTISEMENT_ID=p.ADVERTISEMENT_ID order by PAYMENT_AMOUNT desc"
        cursor.execute(sql)
        result = cursor.fetchall()
        #.close()
        for r in result:
            product_id=r[4]
            product_name = r[0]
            price = r[2]
            device_catagory = r[1]
            condition = r[3]
            row = {'product_name': product_name, 'device_catagory': device_catagory,
                'price': price, 'condition': condition,'product_id':product_id}
            dict_result.append(row)
    elif id == 2:
        cursor = conn.cursor()
        sql = "SELECT pr.PRODUCT_NAME,p.PET_TYPE,price,pr.product_id FROM product pr,pet p,ADVERTISEMENT ad WHERE pr.PRODUCT_ID=p.PRODUCT_ID and ad.ADVERTISEMENT_ID=pr.ADVERTISEMENT_ID order by PAYMENT_AMOUNT desc"
        cursor.execute(sql)
        result = cursor.fetchall()
        #cursor.close()
        for r in result:
            product_id=r[3]
            product_name = r[0]
            price = r[2]
            pet_type = r[1]
            row = {'product_name': product_name,
                'pet_type': pet_type, 'price': price,'product_id':product_id}
            dict_result.append(row)
    elif id == 3:
        cursor = conn.cursor()
        sql = "SELECT pr.PRODUCT_NAME,b.genre,condition, price,pr.product_id FROM product pr,book b,ADVERTISEMENT ad WHERE pr.PRODUCT_ID=b.PRODUCT_ID and ad.ADVERTISEMENT_ID=pr.ADVERTISEMENT_ID order by PAYMENT_AMOUNT desc"
        cursor.execute(sql)
        result = cursor.fetchall()
        #cursor.close()
        for r in result:
            product_id=r[4]
            product_name = r[0]
            price = r[3]
            genre= r[1]
            condition=r[2]
            row = {'product_name': product_name,
                'genre': genre, 'price': price,'condition': condition,'product_id':product_id}
            dict_result.append(row)
    elif id == 4:
        cursor = conn.cursor()
        sql = "SELECT pr.PRODUCT_NAME,COURSE_TITLE,price,pr.product_id FROM product pr,course c,ADVERTISEMENT ad WHERE pr.PRODUCT_ID=c.PRODUCT_ID and ad.ADVERTISEMENT_ID=pr.ADVERTISEMENT_ID order by PAYMENT_AMOUNT desc"
        cursor.execute(sql)
        result = cursor.fetchall()
        #cursor.close()
        for r in result:
            product_id=r[3]
            product_name = r[0]
            price = r[2]
            course_title=r[1]
            row = {'product_name': product_name,
                'price': price,'course_title': course_title,'product_id':product_id}
            dict_result.append(row)
    elif id == 5:
        cursor = conn.cursor()
        sql = "SELECT pr.PRODUCT_NAME,TUTOR_GENDER,EDUCATION_LEVEL,price,pr.product_id FROM product pr,tution t,ADVERTISEMENT ad  WHERE pr.PRODUCT_ID=t.PRODUCT_ID and ad.ADVERTISEMENT_ID=pr.ADVERTISEMENT_ID order by PAYMENT_AMOUNT desc"
        cursor.execute(sql)
        result = cursor.fetchall()
        #cursor.close()
        for r in result:
            product_id=r[4]
            product_name = r[0]
            price = r[3]
            tutor_gender= r[1]
            education_level=r[2]
            row = {'product_name': product_name,
                'tutor_gender': tutor_gender, 'price': price,'education_level': education_level,'product_id':product_id}
            dict_result.append(row)
    params={'products':dict_result,'id':id}
    conn.close()
    return render(request,'product/listProduct.html',params)

def displayProduct(request,id,product_id):
    dsn_tns  = cx_Oracle.makedsn('localhost','1521',service_name='ORCL')
    conn = cx_Oracle.connect(user='bikroy',password='bikroy',dsn=dsn_tns)
    #product_id='pr'+str(product_id)
    params={}
    if id==1:
        cursor = conn.cursor()
        sql = "SELECT PRODUCT_NAME,price,DESCRIPTION,CONTACT_NO,DEVICE_CATAGORY,BRAND,MODEL,GENERATION,FEATURES,condition,AUTHENTICITY,PAYMENT_SYSTEM,TO_CHAR(AD_TIME,'dd MON YYYY '), FIRST_NAME||' '||LAST_NAME,THANA,DISTRICT,DIVISION from PRODUCT pr,DEVICES d,ADVERTISEMENT ad,account ac,profile pf,LOCATION l where pr.PRODUCT_ID=d.PRODUCT_ID and ac.USERNAME=ad.USERNAME and ac.PROFILE_NO=pf.PROFILE_NO and pf.LOCATION_ID=l.LOCATION_ID and pr.ADVERTISEMENT_ID=ad.ADVERTISEMENT_ID and pr.PRODUCT_ID= :prid"
        cursor.execute(sql,prid=product_id)
        result = cursor.fetchall()
        #print(result)
        #cursor.close()
        for r in result:
            product_name=r[0]
            price=r[1]
            description=r[2]
            contact_no=r[3]
            device_catagory=r[4]
            brand=r[5]
            model=r[6]
            generation=r[7]
            features=r[8]
            condition=r[9]
            authenticity=r[10]
            fullname=r[13]
            payment_system=r[11]
            ad_time=r[12]
            thana=r[14]
            district=r[15]
            division=r[16]
        params={'product_id':product_id,'product_name':product_name,'price':price,'description':description,'contact_no':contact_no,'device_catagory':device_catagory,' brand': brand,'model':model,'generation':generation,'features':features,'condition':condition,'authenticity':authenticity,'fullname':fullname,'payment_system':payment_system,'ad_time':ad_time,'thana':thana,'district':district,'division':division,'id':id}
    elif id==2:
        cursor = conn.cursor()
        sql = "SELECT PRODUCT_NAME,price,DESCRIPTION,CONTACT_NO,pet_type,color,age, p.gender,FOOD_HABIT,PAYMENT_SYSTEM,TO_CHAR(AD_TIME, 'dd MON YYYY '), FIRST_NAME||' '||LAST_NAME,THANA,DISTRICT,DIVISION from PRODUCT pr,pet p,ADVERTISEMENT ad,account ac,profile pf,LOCATION l where pr.PRODUCT_ID=p.PRODUCT_ID and ac.USERNAME=ad.USERNAME and ac.PROFILE_NO=pf.PROFILE_NO and pf.LOCATION_ID=l.LOCATION_ID and pr.ADVERTISEMENT_ID=ad.ADVERTISEMENT_ID and pr.PRODUCT_ID=:prid"
        cursor.execute(sql,prid=product_id)
        result = cursor.fetchall()
        #print(result)
        #cursor.close()
        for r in result:
            product_name=r[0]
            price=r[1]
            description=r[2]
            contact_no=r[3]
            pet_type=r[4]
            color=r[5]
            age=r[6]
            gender=r[7]
            food_habit=r[8]
            fullname=r[11]
            payment_system=r[9]
            ad_time=r[10]
            thana=r[12]
            district=r[13]
            division=r[14]
        params={'product_id':product_id,'product_name':product_name,'price':price,'description':description,'contact_no':contact_no,'pet_type':pet_type,' age': age,'color':color,'food_habit':food_habit,'gender':gender,'fullname':fullname,'payment_system':payment_system,'ad_time':ad_time,'thana':thana,'district':district,'division':division,'id':id}
    elif id==3:
        cursor = conn.cursor()
        sql = "SELECT PRODUCT_NAME,price,DESCRIPTION,CONTACT_NO,WRITER,GENRE,CONDITION,PAYMENT_SYSTEM,TO_CHAR(AD_TIME, 'dd MON YYYY '), FIRST_NAME||' '||LAST_NAME,THANA,DISTRICT,DIVISION from PRODUCT pr,book b,ADVERTISEMENT ad,account ac,profile pf,LOCATION l where pr.PRODUCT_ID=b.PRODUCT_ID and ac.USERNAME=ad.USERNAME and ac.PROFILE_NO=pf.PROFILE_NO and pf.LOCATION_ID=l.LOCATION_ID and pr.ADVERTISEMENT_ID=ad.ADVERTISEMENT_ID and pr.PRODUCT_ID=:prid"
        cursor.execute(sql,prid=product_id)
        result = cursor.fetchall()
        #print(result)
        #cursor.close()
        for r in result:
            product_name=r[0]
            price=r[1]
            description=r[2]
            contact_no=r[3]
            writer=r[4]
            genre=r[5]
            condition=r[6]
            payment_system=r[7]
            ad_time=r[8]
            fullname=r[9]
            thana=r[10]
            district=r[11]
            division=r[12]
        params={'product_id':product_id,'product_name':product_name,'price':price,'description':description,'contact_no':contact_no,'writer':writer,'condition':condition,'genre':genre,'fullname':fullname,'payment_system':payment_system,'ad_time':ad_time,'thana':thana,'district':district,'division':division,'id':id}
    elif id==4:
        cursor = conn.cursor()
        sql = "SELECT PRODUCT_NAME,price,DESCRIPTION,CONTACT_NO,COURSE_TITLE,c.ORGANIZATION,PAYMENT_SYSTEM,TO_CHAR(AD_TIME, 'dd MON YYYY '), FIRST_NAME||' '||LAST_NAME,THANA,DISTRICT,DIVISION from PRODUCT pr,COURSE c,ADVERTISEMENT ad,account ac,profile pf,LOCATION l where pr.PRODUCT_ID=c.PRODUCT_ID and ac.USERNAME=ad.USERNAME and ac.PROFILE_NO=pf.PROFILE_NO and pf.LOCATION_ID=l.LOCATION_ID and pr.ADVERTISEMENT_ID=ad.ADVERTISEMENT_ID and pr.PRODUCT_ID=:prid"
        cursor.execute(sql,prid=product_id)
        result = cursor.fetchall()
        #print(result)
        #cursor.close()
        for r in result:
            product_name=r[0]
            price=r[1]
            description=r[2]
            contact_no=r[3]
            course_title=r[4]
            organization=r[5]
            fullname=r[8]
            payment_system=r[6]
            ad_time=r[7]
            thana=r[9]
            district=r[10]
            division=r[11]
        params={'product_id':product_id,'product_name':product_name,'price':price,'description':description,'contact_no':contact_no,'course_title':course_title,'organization':organization,'fullname':fullname,'payment_system':payment_system,'ad_time':ad_time,'thana':thana,'district':district,'division':division,'id':id}
    elif id==5:
        cursor = conn.cursor()
        sql = "SELECT PRODUCT_NAME,price,DESCRIPTION,CONTACT_NO,TUTION_SUBJECT,TIME_DURATION,TUTOR_GENDER,EDUCATION_LEVEL,PAYMENT_SYSTEM,TO_CHAR(AD_TIME, 'dd MON YYYY '), FIRST_NAME||' '||LAST_NAME,THANA,DISTRICT,DIVISION from PRODUCT pr,TUTION t,ADVERTISEMENT ad,account ac,profile pf,LOCATION l where pr.PRODUCT_ID=t.PRODUCT_ID and ac.USERNAME=ad.USERNAME and ac.PROFILE_NO=pf.PROFILE_NO and pf.LOCATION_ID=l.LOCATION_ID and pr.ADVERTISEMENT_ID=ad.ADVERTISEMENT_ID and pr.PRODUCT_ID=:prid"
        cursor.execute(sql,prid=product_id)
        result = cursor.fetchall()
        #print(result)
        #cursor.close()
        for r in result:
            product_name=r[0]
            price=r[1]
            description=r[2]
            contact_no=r[3]
            subject=r[4]
            time=r[5]
            t_gender=r[6]
            edu_level=r[7]
            fullname=r[10]
            payment_system=r[8]
            ad_time=r[9]
            thana=r[11]
            district=r[12]
            division=r[13]
        params={'product_id':product_id,'product_name':product_name,'price':price,'description':description,'contact_no':contact_no,'tution_subject':subject,'tutor_gender':t_gender,'time_duration':time,'education_level':edu_level, 'fullname':fullname,'payment_system':payment_system,'ad_time':ad_time,'thana':thana,'district':district,'division':division,'id':id}  
    conn.close()
    return render(request,'product/displayProduct.html',params)





        

     



        