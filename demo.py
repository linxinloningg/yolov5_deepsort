from AIDetector_pytorch import Detector
import imutils
import cv2


def main():
    name = 'demo'

    det = Detector()
    cap = cv2.VideoCapture('test.mp4')
    fps = int(cap.get(5))

    while True:

        try:
            _, im = cap.read()
            if im is None:
                break

            result = det.feedCap(im)
            result = result['frame']
            result = imutils.resize(result, height=500)

            fourcc = cv2.VideoWriter_fourcc(
                'm', 'p', '4', 'v')  # opencv3.0

            video_writer = cv2.VideoWriter(
                'result.mp4', fourcc, fps, (result.shape[1], result.shape[0]))

            video_writer.write(result)
            cv2.imshow(name, result)
            cv2.waitKey(1)

            if cv2.getWindowProperty(name, cv2.WND_PROP_AUTOSIZE) < 1:
                # 点x退出
                cap.release()
                video_writer.release()
                cv2.destroyAllWindows()
                break

        except Exception as e:
            print(e)
            continue


if __name__ == '__main__':
    main()
