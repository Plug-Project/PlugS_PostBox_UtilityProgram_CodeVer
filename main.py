import webview, configparser, pymysql, random
from discord_webhook import *

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/gh/sun-typeface/SUITE/fonts/static/woff2/SUITE.css" rel="stylesheet">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <style>
        * {
            font-family: 'SUITE', sans-serif;
            -webkit-user-select: none;
            -moz-user-select: none;
            -ms-user-select: none;
            user-select: none
        }

        .postBox {
            display: block;
            width: 350px;
            height: 500px;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: #CCCFD8;
        }

        .postBox>.postBoxHeader {
            text-align: center;
            font-size: 20px;
            font-weight: 500;
            background-color: #282F3D;
            padding: 8px;
            color: white;
            margin-bottom: 8px;
        }

        .postBox>.userInfoText {
            margin-left: 8px;
            font-size: 14px;
            font-weight: 600;
            color: #173674
        }

        .postBoxLeft {
            width: 350px;
            height: 500px;
            position: absolute;
            top: 50%;
            left: 68.2%;
            transform: translate(-50%, -50%);
            background-color: #CCCFD8;
        }

        .postBoxLeft>.postBoxHeader {
            text-align: center;
            font-size: 20px;
            font-weight: 600;
            background-color: #282F3D;
            padding: 8px;
            color: white;
        }

        .postBoxLeft>.postTitleBox {
            display: flex;
            flex-direction: column;
            justify-content: center;
            height: 50px;
            margin: 36px 16px 1px 16px;
            background-color: #EBEEF4;
        }

        .itemRewardTitle {
            color: #282F3D;
            font-size: 13px;
            font-weight: 600;
        }

        .postBoxLeft>.postContentBox {
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding: 8px;
            margin: 0px 16px 2px 16px;
            background-color: #EBEEF4;
        }

        .postBoxLeft>.buttonPostion {
            position: absolute;
            right: 10px;
            bottom: 10px;
        }

        .postBoxLeft > .postContentBox > .content > .itemRewardBox {
            margin-top: 8px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
        }

        .postBoxLeft > .postContentBox > .content > .itemRewardBox > .itemInfo {
            display: flex;
            align-items: center;
        }

        .postBoxLeft > .postContentBox > .content > .itemRewardBox > .itemInfo > .itemImage {
            width: 30px;
            height: 30px;
            background-color: #303030;
            margin-right: 10px;
        }

        .postBoxLeft > .postContentBox > .content > .itemRewardBox > .itemInfo > .itemImage > img {
            width: 15px;
            height: 15px;
        }

        .postBoxLeft > .postContentBox > .content > .itemRewardBox > .itemInfo > .itemName, .itemCount {
            margin-right: 10px;
        }

        .postBoxLeft>.buttonPostion>.itemRewardButton {
            height: 30;
            width: 90;
            border: 2px solid #282F3D;
            background-color: #282F3D;
            color: white;
            padding: 5px 10px;
            cursor: pointer;
        }

        .postBoxLeft>.buttonPostion>.itemRewardClose {
            height: 30;
            width: 90;
            border: 2px solid #4F4F4F;
            background-color: #4F4F4F;
            color: white;
            padding: 5px 10px;
            cursor: pointer;
        }

        .mailPost {
            display: flex;
            align-items: center;
            margin: 8px;
        }

        .imageBox {
            width: 50px !important;
            height: 50px !important;
            min-width: 50px !important;
            min-height: 50px !important;
            max-width: 50px !important;
            max-height: 50px !important;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #303030;
        }

        .imageBox img {
            width: 40px;
            height: 40px;
            object-fit: cover;
            object-position: center;
        }

        .textContents {
            display: flex;
            flex-direction: column;
            justify-content: center;
            width: 100%;
            height: 50px;
            background-color: #EBEEF4;
        }

        .title,
        .description {
            margin-left: 8px;
        }

        .title {
            font-size: 13px;
            font-weight: 500;
            margin-bottom: 2px;
        }

        .description {
            font-size: 13px;
            font-weight: 500;
            color: #777777;
        }

        .content {
            font-size: 13px;
            font-weight: 500;
        }

        .warningNotify {
            display: none;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: #7D7D7D;
            text-align: center;
            font-size: 13px;
            font-weight: 500;
        }
        .sideMenuBar {
            position: fixed;
            left: 0;
            top: 50%;
            transform: translateY(-50%);
            display: flex;
            flex-direction: column;
            align-items: center;
            background-color: #EBEEF4;
            padding: 20px;
        }
        .itemInputGroup {
            display: flex;
            align-items: center;
            margin-bottom: 10px;
        }

        .itemInputGroup label {
            margin-right: 10px;
        }

        input {
            width: 200px;
            height: 30px;
            border-top: none;
            border-left: none;
            border-right: none;
            border-bottom : 3px solid black;
        }

        textarea {
            width: 300px;
            height: 100px;
            resize: none;
            color: black;
            border: none;
            border-bottom : 3px solid black;
            outline: none;
        }

        .seechxnBtn {
            height: auto;
            width: auto;
            padding: 8px;
            border: 2px solid #282F3D;
            background-color: #282F3D;
            color: white;
            padding: 5px 10px;
            cursor: pointer;
        }
        
    </style>
</head>
<body>
    <div class="postBox">
        <div class="postBoxHeader">우편함</div>
        <span class="userInfoText">플러그(1) 님의 우편</span>
        <div class="mailPost" id="123123">
            <div class="imageBox">
                <img src="https://cdn-icons-png.flaticon.com/512/6521/6521826.png" />
            </div>
            <div class="textContents">
                <span class="title">불러오는 중...</span>
                <span class="description">불러오는 중...</span>
            </div>
        </div>
    </div>

    <script>
        let itemList = [];
        var tempJsonData = {};

        $(document).ready(function () {
            var lastClickedId = null;

            $(document).on('click', '.mailPost', function () {
                var clickedId = $(this).attr('id');

                if (clickedId === lastClickedId) {
                    $('.postBoxLeft').remove();
                    lastClickedId = null;
                } else {
                    $('.postBoxLeft').remove();
                    var $postBoxLeft = $(`
                        <div class="postBoxLeft">
                            <div class="postBoxHeader">받은 우편</div>
                            <div class="postTitleBox">
                                <span class="title">보낸 사람 : 치즈 운영팀</span>
                                <span class="title" id="postTitleBoxTitle">제목 : 불러오는 중...</span>
                            </div>
                            <div class="postContentBox">
                                <span class="content">
                                    <span id="postContentBoxText">불러오는 중...</span>
                                    <br></br>
                                    <br></br>
                                    <span class="itemRewardTitle">받은 아이템</span>
                                    <div class="content" id="itemListContainer"></div>
                                </span>
                            </div>
                            <div class="buttonPostion">
                                <button class="itemRewardButton" onclick="itemReward(${clickedId})">보상 수령</button>
                                <button class="itemRewardClose">닫기</button>
                            </div>
                        </div>
                    `);
                    $('body').append($postBoxLeft);
                    lastClickedId = clickedId;
                }
            });
        });

        window.addEventListener('message', function (event) {
            const data = event.data;
            if (data.type === 'updatePreview') {
                $(".title").text(data.title);
                $(".description").text(data.description);
                $("#postTitleBoxTitle").text(`제목 : ${data.title}`);
                $("#postContentBoxText").html(data.postContent);
                $("#itemListContainer").empty();
                tempJsonData = JSON.stringify({title: data.title, subTitle: data.description, description: (data.postContent).replace(/\\r\\n|\\n|\\r/gm, "<br>"), itemList: data.itemList});
                const postContainer = document.querySelector('.content');
                data.itemList.forEach(post => {
                    const postHTML = `
                        <div class="itemRewardBox">
                            <div class="itemInfo">
                                <img class="itemImage" src="https://cdn-icons-png.flaticon.com/512/6521/6521826.png" onerror="noImage()" />
                                <span class="itemName">${post.itemName}</span>
                            </div>
                            <span class="itemCount">${post.itemAmount}</span>
                        </div>
                    `;
                    postContainer.innerHTML += postHTML;
                });
            } else if (data.type === 'customAlert') {
                alert(data.msg);
            }
        });


        function sendUpdate() {
            const title = $("#inputTitle").val();
            const description = $("#inputDescription").val();
            const postContent = $("#inputPostContent").val();
            $(".itemRewardBox").remove();
            window.pywebview.api.update_preview(title, description, postContent, itemList);
        }

        function grantAll() {
            window.pywebview.api.grant_all(tempJsonData);
        }

        function grantBatch() {
            var user_id = prompt('지급 대상 고유번호를 작성하여 주세요.', '123');
            window.pywebview.api.grant_batch(tempJsonData, user_id);
        }

        function addItem() {
            const itemImage = "PlugS.png";
            const itemCode = $("#inputItemCode").val();
            const itemName = $("#inputItemName").val();
            const itemAmount = $("#inputItemAmount").val();
            if (!itemCode=="" && !itemName=="" && !itemAmount=="") {
                itemList.push({ itemImage, itemCode, itemName, itemAmount });
                displayItemList();
            } else {
                alert("양식에 맞게 작성 하여 주시기 바랍니다.")
            }
        }

        function removeItem(index) {
            itemList.splice(index, 1);
            displayItemList();
        }

        function displayItemList() {
            $("#itemListDisplay").empty();
            itemList.forEach((item, index) => {
                const itemHTML = `
                    <div style="margin-bottom: 8px;">
                        <span>${item.itemName} (${item.itemAmount})</span>
                        <button class="seechxnBtn" onclick="removeItem(${index})">Remove</button>
                    </div>
                `;
                $("#itemListDisplay").append(itemHTML);
            });
        }
    </script>

    <div class="sideMenuBar">
        <label>우편함 제목</label>
        <input type="text" id="inputTitle" required><br>
        <label for="inputDescription">우편함 서브제목</label>
        <input type="text" id="inputDescription" required><br>
        <label for="inputPostContent">우편함 설명</label>
        <textarea id="inputPostContent" cols="30" rows="5" required></textarea><br>
        <label>우편함 지급 아이템</label>
        <div class="itemInputGroup">
            <input type="text" id="inputItemCode" placeholder="지급할 아이템코드" required>, 
            <input type="text" id="inputItemName" placeholder="지급할 아이템이름" required>, 
            <input type="text" id="inputItemAmount" placeholder="지급할 갯수" required>
        </div>
        <button class="seechxnBtn" onclick="addItem()">아이템 추가하기</button>
        <div id="itemListDisplay" style="margin-top: 10px;"></div>
        <br />
        <button class="seechxnBtn" onclick="sendUpdate()">프리뷰 새로고침</button>
        <br>
        <div class="itemInputGroup">
            <button class="seechxnBtn" onclick="grantAll()">모두 지급</button>
            <div style="width: 28px"></div>
            <button class="seechxnBtn" onclick="grantBatch()">일괄 지급</button>
        </div>
    </div>

</body>
</html>
"""

config = configparser.ConfigParser()
print(f"{config.read('Config.ini')[0]}의 읽기가 완료 되었습니다.")

class Api:
    def update_preview(self, title, description, post_content, item_list):
        data = {
            'type': 'updatePreview',
            'title': title,
            'description': description,
            'postContent': post_content,
            'itemList': item_list
        }
        window.evaluate_js(f"window.postMessage({data}, '*');")
    
    def customAlert(self, msg):
        data = {
            'type': 'customAlert',
            'msg': msg
        }
        window.evaluate_js(f"window.postMessage({data}, '*');")

    def grant_all(self, data):
        seechxn.addAllUser(data)

    def grant_batch(self, data, user_id):
        seechxn.addAuthorUser(user_id, data)

class seechxn:
    def get_SQL():
        try:
            db = pymysql.connect(
                host=config.get("MYSQL", "HOST"), 
                user=config.get("MYSQL", "USER"), 
                password=config.get("MYSQL", "PW"), 
                db=config.get("MYSQL", "DB"), 
                charset="utf8"
            )
            SQL = db.cursor()
            return db, SQL
        
        except Exception as e:
            print(e)
            return False, False
    
    def addAllUser(postData):
        db, SQL = seechxn.get_SQL()
        if not db and not SQL:
            return Api().customAlert("데이터베이스와 연결이 불안정 합니다.")
        try:

            SQL.execute("SELECT id FROM vrp_users")
            user_ids = SQL.fetchall()
            
            for user_id in user_ids:
                SQL.execute(f"INSERT INTO seechxn_postbox(user_id, post_id, post_data) VALUES ('{user_id[0]}', '{random.randint(100, 999999)}', '{postData}')")

            db.commit()
            Api().customAlert("모든 유저에게 정사적으로 적용 하였습니다.")
        
        except Exception as e:
            Api().customAlert(f"{e}")
    
    def addAuthorUser(user_id, postData):
        db, SQL = seechxn.get_SQL()
        if not db and not SQL:
            return Api().customAlert("데이터베이스와 연결이 불안정 합니다.")
        
        try:
            SQL.execute(f"INSERT INTO seechxn_postbox(user_id, post_id, post_data) VALUES ('{user_id}', '{random.randint(100, 999999)}', '{postData}')")
            db.commit()
            Api().customAlert(f"{user_id}번 에게 정상적으로 적용 하였습니다.")
        
        except Exception as e:
                Api().customAlert(f"{e}")

api = Api()
window = webview.create_window('PlugS_PostBox - Preview', html=html_code, js_api=api)
webview.start()