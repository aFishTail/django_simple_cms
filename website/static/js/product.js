// 设置分类tab 激活状态
function setActivateTab() {
    category_id = $.getUrlQuery('category_id')
    if (category_id) {
        $('#categoryTab .nav-link').each(function (index) {
            const data = $(this).attr('data')
            if (data === category_id) {
                $(this).addClass('active')
            }
        })
    }
}

// 设置面包屑
function setBreadcrumb() {
        category_id = $.getUrlQuery('category_id')
    if (!category_id) {
        $('.breadcrumb').append($('<li class="breadcrumb-item active" aria-current="page">产品中心</li>'))
    } else {
        $('.breadcrumb').append($('<li class="breadcrumb-item active" aria-current="page">产品中心</li>'))
    }
}

$(function () {
    setActivateTab()
    // setBreadcrumb()
})