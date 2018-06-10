$().ready(function () {
    check();
    load();
});

//加载所有课程信息
function load() {
    $.ajax({
        type: 'GET',
        url: '/course/getAll/',
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
                    'chooseClass("' + resultList[i].getElementsByTagName("课程编号")[0].firstChild.nodeValue + '", ' + i + ')' +
                    '});' +
                    '</script>'
                );
            }
        },
        error: function (xhr, status, error) {
            console.log(xhr.status);
        }

    })
}

//选课
function chooseClass(c_id, i) {
    $.ajax({
        type: 'GET',
        url: '/course/select/',
        data: {
            sid: localStorage.getItem('account'),
            cid: c_id
        },
        success: function (result) {
            if (result) {
                $('#chosen_' + i).show();
                $('#choose_' + i).hide();
            } else {
              alert("已选择该课程，请勿重复选课 !");
            }
        },
        error: function (xhr, status, error) {
            console.log(xhr.status);
        }
    })
}