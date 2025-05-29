from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        emotions_dict_1 = emotion_detector("I am glad this happened")
        self.assertEqual(emotions_dict_1["dominant_emotion"], "joy")
        emotions_dict_2 = emotion_detector("I am really mad about this")
        self.assertEqual(emotions_dict_2["dominant_emotion"], "anger")
        emotions_dict_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(emotions_dict_3["dominant_emotion"], "disgust")
        emotions_dict_4 = emotion_detector("I am so sad about this")
        self.assertEqual(emotions_dict_4["dominant_emotion"], "sadness")
        emotions_dict_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(emotions_dict_5["dominant_emotion"], "fear")

unittest.main()