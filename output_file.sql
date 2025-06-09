CREATE TABLE IF NOT EXISTS `employees` (
    `CustomerID` INTEGER,
    `CustomerName` TEXT,
    `ContactPerson` TEXT,
    `PhoneNumber` INTEGER,
    `Email` TEXT,
    `Address` TEXT
);

INSERT INTO `employees` (`CustomerID`, `CustomerName`, `ContactPerson`, `PhoneNumber`, `Email`, `Address`) VALUES
(1, 'ABC Company', 'John Doe', 123455, NULL, '123 Main St, City1'),
(2, 'XYZ Corporation', 'Jane Smith', 987654321, 'janesmith@xyz.com', '456 Elm St, City2'),
(3, '王五', '王五', 13700337003, 'wangwu@example.com', '广州市天河区珠江新城'),
(4, '赵六', '赵六', 13600436004, 'zhaoliu@example.com', '深圳市南山区科技园'),
(5, '孙七', '孙七', 13500535005, 'sunqi@example.com', '杭州市西湖区文三路'),
(6, '周八', '周八', 13400634006, 'zhouba@example.com', '成都市武侯区天府软件园'),
(7, '吴九', '吴九', 13300733007, 'wujiu@example.com', '南京市玄武区珠江路'),
(8, '郑十', '郑十', 13200832008, 'zhengshi@example.com', '武汉市洪山区珞喻路'),
(9, '王二', '王二', 13100931009, 'wanger@example.com', '重庆市渝中区解放碑'),
(10, '李三', '李三', 13001030010, 'lisan@example.com', '西安市雁塔区小寨'),
(11, '陈四', '陈四', 13801138011, 'chensi@example.com', '长沙市岳麓区麓谷'),
(12, '刘五', '刘五', 13901239012, 'liuwu@example.com', '青岛市市南区东海路'),
(13, '杨六', '杨六', 13701337013, 'yangliu@example.com', '天津市和平区滨江道'),
(14, '何七', '何七', 13601436014, 'heqi@example.com', '苏州市工业园区星湖街'),
(15, '赵八', '赵八', 13501535015, 'zhaoba@example.com', '厦门市思明区软件园'),
(16, '孙九', '孙九', 13401634016, 'sunjiu@example.com', '郑州市金水区文化路'),
(17, '周十', '周十', 13301733017, 'zhoushi@example.com', '福州市鼓楼区五四路'),
(18, '吴二', '吴二', 13201832018, 'wuer@example.com', '南昌市红谷滩新区'),
(19, '郑三', '郑三', 13101931019, 'zhengsan@example.com', '昆明市五华区青年路'),
(20, '王四', '王四', 13002030020, 'wangsi@example.com', '哈尔滨市道里区中央大街');