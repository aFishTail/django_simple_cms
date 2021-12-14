function getUrlQuery(key) {
  let map = new Map()
  let keyMap = window.location.search.substring(1).split('&').forEach(e => {
    const list = e.split('=')
    map.set(list[0], list[1])
  })
  return map.get(key)
}

$.getUrlQuery = getUrlQuery