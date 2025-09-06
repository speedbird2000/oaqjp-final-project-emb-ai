import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        test_1=emotion_detector("I am glad this happened")
        self.assertEqual(test_1['dominant']['label'], "joy")
        test_2=emotion_detector("I am really mad about this")
        self.assertEqual(test_2['dominant']['label'], "anger")
        test_3=emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(test_3['dominant']['label'], "disgust")
        test_4=emotion_detector("I am so sad about this")
        self.assertEqual(test_4['dominant']['label'], "sadness")
        test_5=emotion_detector("I am really afraid that this wil happen")
        self.assertEqual(test_5['dominant']['label'], "fear")

unittest.main()




