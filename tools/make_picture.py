import cv2
from tools.get_log import GetLog

log = GetLog.get_logger()

# 滑块拼接图片处理类
log.info("滑块拼接图片处理类")


class Make_Picture:
    # 对图片进行灰度、模糊处理
    log.info("调用图片进行灰度、模糊处理方法")

    def make_picture(self, pic):
        # 转灰度图
        picGray = cv2.cvtColor(pic, cv2.COLOR_RGBA2GRAY)
        # 高斯模糊
        picBlur = cv2.GaussianBlur(picGray, (5, 5), 1)
        # Canny算子边缘检测
        picCanny = cv2.Canny(picBlur, 60, 60)
        # 返回处理结果
        log.info("返回处理结果")
        return picCanny

    # 获取图像移动距离
    log.info("获取图像移动距离")

    def Measure_distance(self, big_path, small_path):
        # 读取图像
        big_pic = cv2.imread(big_path, cv2.IMREAD_UNCHANGED)
        small_pic = cv2.imread(small_path, cv2.IMREAD_UNCHANGED)
        # 调用上边方法处理图片
        big_masu = self.make_picture(big_pic)
        small_masu = self.make_picture(small_pic)
        res_TM_CCOEFF_NORMED = cv2.matchTemplate(big_masu, small_masu, 3)
        value = cv2.minMaxLoc(res_TM_CCOEFF_NORMED)
        # 获取到移动距离
        value = value[3][0]
        # 返回获取的距离
        log.info("返回获取的距离" + str(value))
        return value


if __name__ == '__main__':
    dd = Make_Picture().Measure_distance('../scripts/shopping/re.png', './can.png')
    print(dd)
