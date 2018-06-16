$().ready(function () {
    // check();
    $('#own').click();
});

$('#own').click(function () {
    $('#own').addClass("active-menu");
    $('#other').removeClass("active-menu");
    $('#view').text("专业选课");
    $('#share').hide();
    load();
});

$('#other').click(function () {
    $('#other').addClass("active-menu");
    $('#own').removeClass("active-menu");
    $('#view').text("跨院系选课");
    $('#share').show();
    $('#college').empty();
});

$('#check').click(function () {
    let dep = $('input[name=dep]:checked').val();

    // loadShareCourse(dep);
});

//加载院系所有课程信息
function load() {
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

                if (resultList[i].getElementsByTagName("a:选择")[0].firstChild.nodeValue === "True"){
                    $('#college').append(
                        '<tr>' +
                        '<td>' + resultList[i].getElementsByTagName("a:课程编号")[0].firstChild.nodeValue + '</td>' +
                        '<td>' + resultList[i].getElementsByTagName("a:课程名称")[0].firstChild.nodeValue + '</td>' +
                        '<td>' + resultList[i].getElementsByTagName("a:学分")[0].firstChild.nodeValue + '</td>' +
                        '<td>' + resultList[i].getElementsByTagName("a:授课老师")[0].firstChild.nodeValue + '</td>' +
                        '<td>' + resultList[i].getElementsByTagName("a:授课地点")[0].firstChild.nodeValue + '</td>' +
                        '<td>' +
                        '<label id="chosen_' + i + '">已选择</label>' +
                        '</td>' +
                        '</tr>'
                    );
                } else {
                    $('#college').append(
                        '<tr>' +
                        '<td>' + resultList[i].getElementsByTagName("a:课程编号")[0].firstChild.nodeValue + '</td>' +
                        '<td>' + resultList[i].getElementsByTagName("a:课程名称")[0].firstChild.nodeValue + '</td>' +
                        '<td>' + resultList[i].getElementsByTagName("a:学分")[0].firstChild.nodeValue + '</td>' +
                        '<td>' + resultList[i].getElementsByTagName("a:授课老师")[0].firstChild.nodeValue + '</td>' +
                        '<td>' + resultList[i].getElementsByTagName("a:授课地点")[0].firstChild.nodeValue + '</td>' +
                        '<td>' +
                        '<button class="btn btn-link" id="choose_' + i + '">选课</button>' +
                        '</td>' +
                        '</tr>' +
                        '<script>' +
                        '$("#choose_' + i + '").click(function() {' +
                        'chooseClass("' + resultList[i].getElementsByTagName("a:课程编号")[0].firstChild.nodeValue + '")' +
                        '});' +
                        '</script>'
                    );
                }

            }
        },
        error: function (xhr, status, error) {
            console.log(xhr.status);
        }

    })
}

//选课
function chooseClass(c_id) {
    $.ajax({
        type: 'GET',
        url: '/course/select/',
        data: {
            sid: localStorage.getItem('account'),
            cid: c_id
        },
        success: function (result) {
            if (result) {
                location.reload();
            } else {
              alert("已选择该课程，请勿重复选课 !");
            }
        },
        error: function (xhr, status, error) {
            console.log(xhr.status);
        }
    })
}