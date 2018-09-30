// 此脚本用于修改图表的参数

// 路线属性
var colorOrWidth  = 3 ; // 0代表既不用色彩也不用宽度来表示值，1代表用色彩，2代表用宽度，3代表二者皆用
var theColorRamp  = ['#FFFFFF', '#FFB1B1', '#FF5C5C', '#FF0000']; // 路线颜色
var theWidthRatio = 0.0005 // 宽度与值的比值

// 固定属性，当该属性没有和值相关，会自动设成如下值
var theColor  = 'rgb(200, 35, 45)'; // 线的颜色
var theWidth  = 1;    // 线的宽度
var theOpac   = 0.3;  // 线的透明度

// 地图相关
var theCenter = [110.64630126953125,33.984220415249744]; // 中心点坐标
var theZoom   = 6; //视角远近 数字

// 动画效果
var effectShow  = true;// 是否展示动画
var theSpeed    = 0;   // 尾迹速度，当尾迹速度不等于 0 时，使用单次循环时间作为速度依据
var thePeriod   = 12;   // 单次循环时间，只有当尾迹速度为 0 时才能生效
var theEffWidth = 1;   // 尾迹宽度
var theEffLength= 0.3; // 尾迹长度

// 百度地图
// 百度地图的accesstoken需要到 html 的第18行 自行进行替换
var mapStyle= [
          {
                    "featureType": "water",
                    "elementType": "all",
                    "stylers": {
                              "color": "#021019"
                    }
          },
          {
                    "featureType": "highway",
                    "elementType": "geometry.fill",
                    "stylers": {
                              "color": "#000000"
                    }
          },
          {
                    "featureType": "highway",
                    "elementType": "geometry.stroke",
                    "stylers": {
                              "color": "#147a92"
                    }
          },
          {
                    "featureType": "arterial",
                    "elementType": "geometry.fill",
                    "stylers": {
                              "color": "#000000"
                    }
          },
          {
                    "featureType": "arterial",
                    "elementType": "geometry.stroke",
                    "stylers": {
                              "color": "#0b3d51"
                    }
          },
          {
                    "featureType": "local",
                    "elementType": "geometry",
                    "stylers": {
                              "color": "#000000"
                    }
          },
          {
                    "featureType": "land",
                    "elementType": "all",
                    "stylers": {
                              "color": "#08304b"
                    }
          },
          {
                    "featureType": "railway",
                    "elementType": "geometry.fill",
                    "stylers": {
                              "color": "#000000"
                    }
          },
          {
                    "featureType": "railway",
                    "elementType": "geometry.stroke",
                    "stylers": {
                              "color": "#08304b"
                    }
          },
          {
                    "featureType": "subway",
                    "elementType": "geometry",
                    "stylers": {
                              "lightness": -70
                    }
          },
          {
                    "featureType": "building",
                    "elementType": "geometry.fill",
                    "stylers": {
                              "color": "#000000"
                    }
          },
          {
                    "featureType": "all",
                    "elementType": "labels.text.fill",
                    "stylers": {
                              "color": "#857f7f"
                    }
          },
          {
                    "featureType": "all",
                    "elementType": "labels.text.stroke",
                    "stylers": {
                              "color": "#000000"
                    }
          },
          {
                    "featureType": "building",
                    "elementType": "geometry",
                    "stylers": {
                              "color": "#022338"
                    }
          },
          {
                    "featureType": "green",
                    "elementType": "geometry",
                    "stylers": {
                              "color": "#062032"
                    }
          },
          {
                    "featureType": "boundary",
                    "elementType": "all",
                    "stylers": {
                              "color": "#1e1c1c"
                    }
          },
          {
                    "featureType": "manmade",
                    "elementType": "geometry",
                    "stylers": {
                              "color": "#022338"
                    }
          },
          {
                    "featureType": "poi",
                    "elementType": "all",
                    "stylers": {
                              "visibility": "off"
                    }
          },
          {
                    "featureType": "all",
                    "elementType": "labels.icon",
                    "stylers": {
                              "visibility": "off"
                    }
          },
          {
                    "featureType": "all",
                    "elementType": "labels.text.fill",
                    "stylers": {
                              "color": "#2da0c6",
                              "visibility": "on"
                    }
          }
]
