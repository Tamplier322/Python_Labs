from Serializers.ser_factory import SerializersFactory, SerializerType

Json = SerializersFactory.create_serializer(SerializerType.JSON)
Xml = SerializersFactory.create_serializer(SerializerType.XML)

while (True):
    print('1. Get from json to answer.json')
    print('2. get from xaml to answer.xml')
    print('3. Json to xaml from answer.json to answer.xml')
    print('4. Xaml to json from answer.xml to answer.json')
    print('Enter 5 to exit')

    opt = input()

    if (opt == '1'):
        fn = input('Input file name ')

        sourse = open(fn, "r")
        data = open("answer.json", "w")
        Json.dump(sourse.read(), data)

        sourse.close()
        data.close()

    elif (opt == '2'):
        fn = input('Input file name ')

        sourse = open(fn, "r")
        data = open("answer.xml", "w")
        Xml.dump(sourse.read(), data)

        sourse.close();
        data.close();

    elif (opt == '3'):
        xml = open("answer.xml", "w")
        json = open("answer.json", "r")

        obj = Json.load(json)
        Xml.dump(obj, xml)

        xml.close()
        json.close()

    elif (opt == '4'):
        xml = open("answer.xml", "r")
        json = open("answer.json", "w")

        obj = Xml.load(xml)
        Json.dump(obj, json)

        xml.close()
        json.close()
    elif (opt == '5'):
        break

    else:
        print('incorrect')