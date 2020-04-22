
import mxnet as mx
from gluoncv import model_zoo, data, utils
from matplotlib import pyplot as plt
ctx = mx.gpu()
classes = ['card']
net = model_zoo.get_model('yolo3_darknet53_voc', pretrained=True)
net.reset_class(classes)
net.collect_params().reset_ctx(ctx)
net.load_parameters("./models/yolo3_darknet53_voc_0190_0.9071.params",ctx=ctx)




x, img = data.transforms.presets.yolo.load_test("../gxk2.jpg", short=608)
print('Shape of pre-processed image:', x.shape)
x = x.as_in_context(ctx)

class_IDs, scores, bounding_boxs = net(x)
print(bounding_boxs[0][0].astype(int))

ax = utils.viz.plot_bbox(img, bounding_boxs[0], scores[0],thresh=0.4,
                         labels=class_IDs[0], class_names=net.classes)
plt.show()
