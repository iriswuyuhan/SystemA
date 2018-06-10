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
        url:'/getStuInfo',
        data:{
            Sno: localStorage.getItem('account')
        },
        success: function (result) {
            let info = parseXML(result).getElementsByTagName("学生信息");
            $("#s_id").text(info.getElementsByTagName("学号")[0].firstChild.nodeValue);
            $('#s_name').text(info.getElementsByTagName("姓名")[0].firstChild.nodeValue);
            $('#gender').text(info.getElementsByTagName("性别")[0].firstChild.nodeValue);
            $('#major').text(info.getElementsByTagName("院系")[0].firstChild.nodeValue);
        },
        error: function (xhr) {
            console.log(xhr);
        }
    })
}

function loadPersonalClass() {
    $.ajax({
        type: 'GET',
        url:'/course/getStu/',
        data:{
            sis: localStorage.getItem('account')
        },
        dataType: 'xml',
        success: function (result) {
            let resultList = parseXML(result).getElementsByTagName("课程");
            for (let i = 0; i < resultList.length; i++) {
                $('#college').append(
                    '<tr>' +
                    '<td>' + resultList[i].getElementsByTagName("课程编号")[0].firstChild.nodeValue + '</td>' +
                    '<td>' + resultList[i].getElementsByTagName("课程名称")[0].firstChild.nodeValue + '</td>' +
                    '<td>' + resultList[i].getElementsByTagName("学分")[0].firstChild.nodeValue + '</td>' +
                    '<td>' + resultList[i].getElementsByTagName("授课老师")[0].firstChild.nodeValue + '</td>' +
                    '<td>' + resultList[i].getElementsByTagName("授课地点")[0].firstChild.nodeValue + '</td>' +
                    '<td>' +
                    '<button class="btn btn-link" id="choose_' + i + '">选课</button>' +
                    '<label id="chosen_' + i + '" style="display: none">已选择</label>' +
                    '</td>' +
                    '</tr>' +
                    '<script>' +
                    '$("#choose_' + i + '").click(function() {' +
                    'deleteSubject("' + resultList[i].getElementsByTagName("课程编号")[0].firstChild.nodeValue + '")' +
                    '});' +
                    '</script>'
                );
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