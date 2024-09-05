export function hueIsInLocalStorage() {
  return localStorage.getItem('hue') !== null
}

export function lightTheme() {
  let theme = localStorage.getItem('theme')
  if (theme === 'light') {
    return true
  }
  return false
}

export function setColorTheme(theme) {
  localStorage.setItem('theme', theme)
}

/* accepts parameters
 * h  Object = {h:x, s:y, v:z}
 * OR
 * h, s, v
 */
export function HSVtoHEX(h, s, v) {
  let rgb = hsvToRgb(h, s, v)

  let r = rgb[0]
  let g = rgb[1]
  let b = rgb[2]
  console.log(rgb)

  return rgbToHex(r, g, b)
}

function hsvToRgb(h, s, v) {
  h /= 360
  v = Math.round(v * 255)
  console.log(h, s, v)

  var i = Math.floor(h * 6)
  var f = h * 6 - i
  var p = Math.round(v * (1 - s))
  var q = Math.round(v * (1 - f * s))
  var t = Math.round(v * (1 - (1 - f) * s))

  switch (i % 6) {
    case 0:
      return [v, t, p]
    case 1:
      return [q, v, p]
    case 2:
      return [p, v, t]
    case 3:
      return [p, q, v]
    case 4:
      return [t, p, v]
    case 5:
      return [v, p, q]
  }
}

function componentToHex(c) {
  var hex = c.toString(16)
  return hex.length == 1 ? '0' + hex : hex
}
function rgbToHex(r, g, b) {
  return '#' + componentToHex(r) + componentToHex(g) + componentToHex(b)
}

export function applyColors() {
  let h = getHue()
  let bgColor
  let fgColor
  let fontColor
  let selectedFontColor
  let inactiveFontColor
  let inactiveFontColorHover
  let inactiveFontColorActive
  let accentColor
  let accentColorHover
  let accentColorActive
  let accentFont
  let accentFontHover
  let accentFontActive
  let innactiveAccentColor
  let innactiveAccentColorHover
  let innactiveAccentColorActive
  let inputBgColor
  let inputFontColor
  let shadowColor

  if (lightTheme()) {
    bgColor = HSVtoHEX(h, 0.02, 0.87)
    fgColor = HSVtoHEX(h, 0.02, 1.0)
    fontColor = HSVtoHEX(h, 1.0, 0.25)
    selectedFontColor = HSVtoHEX(h, 1.0, 0.25)
    inactiveFontColor = HSVtoHEX(h, 1.0, 0.25) + '00'
    inactiveFontColorHover = HSVtoHEX(h, 1.0, 0.25) + '17'
    inactiveFontColorActive = HSVtoHEX(h, 1.0, 0.25) + '29'
    accentColor = HSVtoHEX(h, 0.14, 1.0)
    accentColorHover = HSVtoHEX(h, 0.15, 0.88)
    accentColorActive = HSVtoHEX(h, 0.3, 1.0)
    accentFont = HSVtoHEX(h, 0.72, 0.82)
    accentFontHover = HSVtoHEX(h, 0.72, 0.82)
    accentFontActive = HSVtoHEX(h, 0.72, 0.82)
    innactiveAccentColor = HSVtoHEX(h, 0.14, 1.0)
    innactiveAccentColorHover = HSVtoHEX(h, 0.15, 0.88)
    innactiveAccentColorActive = HSVtoHEX(h, 0.3, 1.0)
    inputBgColor = HSVtoHEX(h, 0.01, 1.0)
    inputFontColor = HSVtoHEX(h, 0.07, 0.05)
    shadowColor = HSVtoHEX(h, 0, 0.63)
  } else {
    bgColor = HSVtoHEX(h, 0.04, 0.11)
    fgColor = HSVtoHEX(h, 0.04, 0.03)
    fontColor = HSVtoHEX(h, 0.15, 0.95)
    selectedFontColor = HSVtoHEX(h, 1.0, 0.95)
    inactiveFontColor = HSVtoHEX(h, 0.15, 0.95) + '00'
    inactiveFontColorHover = HSVtoHEX(h, 0.15, 0.95) + '17'
    inactiveFontColorActive = HSVtoHEX(h, 0.15, 0.95) + '29'
    accentColor = HSVtoHEX(h, 0.15, 1.0)
    accentColorHover = HSVtoHEX(h, 0.15, 0.88)
    accentColorActive = HSVtoHEX(h, 0.3, 1.0)
    accentFont = HSVtoHEX(h, 0.72, 0.82)
    accentFontHover = HSVtoHEX(h, 0.72, 0.82)
    accentFontActive = HSVtoHEX(h, 0.72, 0.82)
    innactiveAccentColor = HSVtoHEX(h, 0.14, 1.0)
    innactiveAccentColorHover = HSVtoHEX(h, 0.15, 0.88)
    innactiveAccentColorActive = HSVtoHEX(h, 0.3, 1.0)
    inputBgColor = HSVtoHEX(h, 0.01, 0.21)
    inputFontColor = HSVtoHEX(h, 0.07, 0.95)
    shadowColor = HSVtoHEX(h, 0.15, 0.15)
  }

  document.documentElement.style.setProperty('--bg-color', bgColor)
  document.documentElement.style.setProperty('--fg-color', fgColor)
  document.documentElement.style.setProperty('--font-color', fontColor)
  document.documentElement.style.setProperty('--selected-font-color', selectedFontColor)
  document.documentElement.style.setProperty('--inactive-font-color', inactiveFontColor)
  document.documentElement.style.setProperty('--inactive-font-color-hover', inactiveFontColorHover)
  document.documentElement.style.setProperty(
    '--inactive-font-color-active',
    inactiveFontColorActive
  )
  document.documentElement.style.setProperty('--accent-color', accentColor)
  document.documentElement.style.setProperty('--accent-color-hover', accentColorHover)
  document.documentElement.style.setProperty('--accent-color-active', accentColorActive)
  document.documentElement.style.setProperty('--accent-font', accentFont)
  document.documentElement.style.setProperty('--accent-font-hover', accentFontHover)
  document.documentElement.style.setProperty('--accent-font-active', accentFontActive)
  document.documentElement.style.setProperty('--inactive-accent-color', innactiveAccentColor)
  document.documentElement.style.setProperty(
    '--inactive-accent-color-hover',
    innactiveAccentColorHover
  )
  document.documentElement.style.setProperty(
    '--inactive-accent-color-active',
    innactiveAccentColorActive
  )
  document.documentElement.style.setProperty('--input-bg-color', inputBgColor)
  document.documentElement.style.setProperty('--input-font-color', inputFontColor)
  document.documentElement.style.setProperty('--shadow-color', shadowColor)
}

export function setHue(hue) {
  localStorage.setItem('hue', hue)
}

export function getHue() {
  if (!hueIsInLocalStorage()) {
    setHue(180)
  }
  return Number(localStorage.getItem('hue'))
}
