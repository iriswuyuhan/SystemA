$().ready(function () {
    check();
    loadPersonalClass();
});

$('#person_info_btn').click(function () {

    document.getElementById("view").innerText = "我的信息";

    $('#person_info').show();
    $('#course_table').hide();

    loadInfo();
});

function loadInfo() {
    $.ajax({
        type: 'GET',
        url:'/student/getStu/',
        data:{
            account: localStorage.getItem('account')
        },
        dataType: 'text',
        success: function (result) {
            let info = parseXML(result).getElementsByTagName("a:学生信息")[0];
            $("#s_id").text(info.getElementsByTagName("a:学号")[0].firstChild.nodeValue);
            $('#s_name').text(info.getElementsByTagName("a:姓名")[0].firstChild.nodeValue);
            $('#gender').text(info.getElementsByTagName("a:性别")[0].firstChild.nodeValue);
            $('#major').text(info.getElementsByTagName("a:院系")[0].firstChild.nodeValue);
        },
        error: function (xhr) {
            console.log(xhr);
        }
    })
}

function loadPersonalClass() {
    $.ajax({
        type: 'GET',
        url: '/course/getStu/',
        data: {
            sid: localStorage.getItem('account')
        },
        dataType: 'text',
        success: function (result) {
            let resultList = parseXML(result).getElementsByTagName("a:课程");
            for (let i = 0; i < resultList.length; i++) {
                console.log(resultList[i].getElementsByTagName("a:选择")[0].firstChild.nodeValue);
                if (resultList[i].getElementsByTagName("a:选择")[0].firstChild.nodeValue === "True"){
                    console.log("success");
                    $('#course_table').append(
                        '<tr>' +
                        '<td>' + resultList[i].getElementsByTagName("a:课程编号")[0].firstChild.nodeValue + '</td>' +
                        '<td>' + resultList[i].getElementsByTagName("a:课程名称")[0].firstChild.nodeValue + '</td>' +
                        '<td>' + resultList[i].getElementsByTagName("a:学分")[0].firstChild.nodeValue + '</td>' +
                        '<td>' + resultList[i].getElementsByTagName("a:授课老师")[0].firstChild.nodeValue + '</td>' +
                        '<td>' + resultList[i].getElementsByTagName("a:授课地点")[0].firstChild.nodeValue + '</td>' +
                        '<td>' +
                        '<button class="btn btn-link" id="choose_' + i + '">退课</button>' +
                        '</td>' +
                        '</tr>' +
                        '<script>' +
                        '$("#choose_' + i + '").click(function() {' +
                        'deleteSubject("' + resultList[i].getElementsByTagName("a:课程编号")[0].firstChild.nodeValue + '")' +
                        '});' +
                        '</script>'
                    );
                }
            }
        },
        error: function (xhr) {
            console.log(xhr);
        }
    })
}




function deleteSubject(c_id) {
    $.ajax({
        type: 'GET',
        url: '/course/drop/',
        data: {
            sid: localStorage.getItem('account'),
            cid: c_id
        },
        success: function (result) {
            if (result) {
                location.reload();
            } else {
                alert("退课失败");
            }
        },
        error: function (xhr) {
            console.log(xhr);
        }
    })
}