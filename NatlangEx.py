
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def language_analysis(text):
        client = language.LanguageServiceClient()   ###  Hashed code is Old code as per video 
        #document = client.document_from_text(text)
        document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)

        #sent_analysis = client.analyze_sentiment()
        sent_analysis = client.analyze_sentiment(document=document).document_sentiment
        print(dir(sent_analysis)) # checking the parameters avaialble
        #sentiment = sent_analysis.sentiment
        #ent_analysis = document.analyze_entities()
        entities = client.analyze_entities(document).entities
        #entities = ent_analysis.entities
        return sent_analysis, entities

#example = u'is it not obvious that python is the best programming language'

### content taken from Python wiki page
example = '''Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python ha
s a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and lar
ge scales.[26]

Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and
 procedural, and has a large and comprehensive standard library.[27]

Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software[28] and has a community-based dev
elopment model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation.'''


sentiment, entities = language_analysis(example)
print('Text: {}'.format(example))
print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
#print(sentiment.score, sentiment.magnit)

entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION', 'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')

for e in entities:
        print(('name', e.name), ('type', entity_type[e.type]), ('metadata', e.metadata), ('salience', e.salience), ('wiki-page', e.metadata.get('wikipedia_url', '-')))

		
		

		
######################### Output ############################		
		
root@gcloud-learning:~/gcloudstuff/natlangex# python natlang.py
['ByteSize', 'Clear', 'ClearExtension', 'ClearField', 'CopyFrom', 'DESCRIPTOR', 'DiscardUnknownFields', 'Extensions', 'FindInitializationErrors', 'FromString', 'HasExtension', 'HasField', 'IsInitialized', 'ListFields', 'MAGNITUDE_FIELD_NUMBER', 'MergeFrom', 'MergeFromString', 'ParseFromString', 'RegisterExtension', 'SCORE_FIELD_NUMBER', 'SerializePartialToString', 'SerializeToString', 'SetInParent', 'WhichOneof', '_CheckCalledFromGeneratedFile', '_SetListener', '__class__', '__deepcopy__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__unicode__', '_extensions_by_name', '_extensions_by_number']
Text: Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales.[26]

Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.[27]

Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software[28] and has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation.
Sentiment: 0.300000011921, 3.09999990463
(('name', u'Python'), ('type', 'ORGANIZATION'), ('metadata', <google.protobuf.pyext._message.ScalarMapContainer object at 0x7f0e0d21a030>), ('salience', 0.6345059275627136), ('wiki-page', u'https://en.wikipedia.org/wiki/Python_(programming_language)'))
(('name', u'CPython'), ('type', 'CONSUMER_GOOD'), ('metadata', <google.protobuf.pyext._message.ScalarMapContainer object at 0x7f0e0ceef620>), ('salience', 0.09657879918813705), ('wiki-page', u'https://en.wikipedia.org/wiki/CPython'))
(('name', u'programming'), ('type', 'OTHER'), ('metadata', <google.protobuf.pyext._message.ScalarMapContainer object at 0x7f0e0ceef670>), ('salience', 0.07697052508592606), ('wiki-page', '-'))
(('name', u'programming language'), ('type', 'OTHER'), ('metadata', <google.protobuf.pyext._message.ScalarMapContainer object at 0x7f0e0cebd670>), ('salience', 0.07367053627967834), ('wiki-page', '-'))
(('name', u'constructs'), ('type', 'OTHER'), ('metadata', <google.protobuf.pyext._message.ScalarMapContainer object at 0x7f0e0cebd620>), ('salience', 0.022070256993174553), ('wiki-page', '-'))
(('name', u'design philosophy'), ('type', 'OTHER'), ('metadata', <google.protobuf.pyext._message.ScalarMapContainer object at 0x7f0e0cebd7b0>), ('salience', 0.01107903104275465), ('wiki-page', '-'))
(('name', u'code readability'), ('type', 'OTHER'), ('metadata', <google.protobuf.pyext._message.ScalarMapContainer object at 0x7f0e0cebd760>), ('salience', 0.01107903104275465), ('wiki-page', '-'))
(('name', u'programming'), ('type', 'OTHER'), ('metadata', <google.protobuf.pyext._message.ScalarMapContainer object at 0x7f0e0cebd800>), ('salience', 0.008617724291980267), ('wiki-page', '-'))
(('name', u'type system'), ('type', 'OTHER'), ('metadata', <google.protobuf.pyext._message.ScalarMapContainer object at 0x7f0e0cebd850>), ('salience', 0.007952776737511158), ('wiki-page', '-'))
(('name', u'whitespace'), ('type', 'CONSUMER_GOOD'), ('metadata', <google.protobuf.pyext._message.ScalarMapContainer object at 0x7f0e0cebd8a0>), ('salience', 0.007587104570120573), ('wiki-page', '-'))
(('name', u'memory management'), ('type', 'OTHER'), ('metadata', <google.protobuf.pyext._message.ScalarMapContainer object at 0x7f0e0cebd8f0>), ('salience', 0.007523048669099808), ('wiki-page', '-'))
(('name', u'programming paradigms'), ('type', 'OTHER'), ('metadata', <google.protobuf.pyext._message.ScalarMapContainer object at 0x7f0e0cebd940>), ('salience', 0.007502541411668062), ('wiki-page', '-'))
(('name', u'scales.'), ('type', 'OTHER'), ('metadata', <google.protobuf.pyext._message.ScalarMapContainer object at 0x7f0e0cebd990>), ('salience', 0.007457780186086893), ('wiki-page', '-'))
(('name', u'Guido van Rossum'), ('type', 'PERSON'), ('metadata', <google.protobuf.pyext._message.ScalarMapContainer object at 0x7f0e0cebd9e0>), ('salience', 0.006572010461241007), ('wiki-page', u'https://en.wikipedia.org/wiki/Guido_van_Rossum'))
(('name', u'development model'), ('type', 'OTHER'), ('metadata', <google.protobuf.pyext._message.ScalarMapContainer object at 0x7f0e0cebda30>), ('salience', 0.005174380727112293), ('wiki-page', '-'))
(('name', u'all'), ('type', 'OTHER'), ('metadata', <google.protobuf.pyext._message.ScalarMapContainer object at 0x7f0e0cebda80>), ('salience', 0.0045772274024784565), ('wiki-page', '-'))
(('name', u'variant implementations'), ('type', 'OTHER'), ('metadata', <google.protobuf.pyext._message.ScalarMapContainer object at 0x7f0e0cebdad0>), ('salience', 0.004126076586544514), ('wiki-page', '-'))
(('name', u'operating systems'), ('type', 'OTHER'), ('metadata', <google.protobuf.pyext._message.ScalarMapContainer object at 0x7f0e0cebdb20>), ('salience', 0.0025923396460711956), ('wiki-page', '-'))
(('name', u'Python interpreters'), ('type', 'PERSON'), ('metadata', <google.protobuf.pyext._message.ScalarMapContainer object at 0x7f0e0cebdbc0>), ('salience', 0.00222200364805758), ('wiki-page', '-'))
(('name', u'Python Software Foundation'), ('type', 'ORGANIZATION'), ('metadata', <google.protobuf.pyext._message.ScalarMapContainer object at 0x7f0e0cebdb70>), ('salience', 0.0021409050095826387), ('wiki-page', u'https://en.wikipedia.org/wiki/Python_Software_Foundation'))
[name: "Python"
type: ORGANIZATION
metadata {
  key: "mid"
  value: "/m/05z1_"
}
metadata {
  key: "wikipedia_url"
  value: "https://en.wikipedia.org/wiki/Python_(programming_language)"
}
salience: 0.634505927563
mentions {
  text {
    content: "Python"
    begin_offset: -1
  }
  type: PROPER
}
mentions {
  text {
    content: "Python"
    begin_offset: -1
  }
  type: PROPER
}
mentions {
  text {
    content: "Python"
    begin_offset: -1
  }
  type: PROPER
}
mentions {
  text {
    content: "Python"
    begin_offset: -1
  }
  type: PROPER
}
, name: "CPython"
type: CONSUMER_GOOD
metadata {
  key: "mid"
  value: "/m/06bxxb"
}
metadata {
  key: "wikipedia_url"
  value: "https://en.wikipedia.org/wiki/CPython"
}
salience: 0.0965787991881
mentions {
  text {
    content: "CPython"
    begin_offset: -1
  }
  type: PROPER
}
mentions {
  text {
    content: "reference implementation"
    begin_offset: -1
  }
  type: COMMON
}
mentions {
  text {
    content: "open source software"
    begin_offset: -1
  }
  type: COMMON
}
mentions {
  text {
    content: "CPython"
    begin_offset: -1
  }
  type: PROPER
}
, name: "programming"
type: OTHER
salience: 0.0769705250859
mentions {
  text {
    content: "programming"
    begin_offset: -1
  }
  type: COMMON
}
, name: "programming language"
type: OTHER
salience: 0.0736705362797
mentions {
  text {
    content: "programming language"
    begin_offset: -1
  }
  type: COMMON
}
, name: "constructs"
type: OTHER
salience: 0.0220702569932
mentions {
  text {
    content: "constructs"
    begin_offset: -1
  }
  type: COMMON
}
, name: "design philosophy"
type: OTHER
salience: 0.0110790310428
mentions {
  text {
    content: "design philosophy"
    begin_offset: -1
  }
  type: COMMON
}
, name: "code readability"
type: OTHER
salience: 0.0110790310428
mentions {
  text {
    content: "code readability"
    begin_offset: -1
  }
  type: COMMON
}
, name: "programming"
type: OTHER
salience: 0.00861772429198
mentions {
  text {
    content: "programming"
    begin_offset: -1
  }
  type: COMMON
}
, name: "type system"
type: OTHER
salience: 0.00795277673751
mentions {
  text {
    content: "type system"
    begin_offset: -1
  }
  type: COMMON
}
, name: "whitespace"
type: CONSUMER_GOOD
salience: 0.00758710457012
mentions {
  text {
    content: "whitespace"
    begin_offset: -1
  }
  type: COMMON
}
, name: "memory management"
type: OTHER
salience: 0.0075230486691
mentions {
  text {
    content: "memory management"
    begin_offset: -1
  }
  type: COMMON
}
, name: "programming paradigms"
type: OTHER
salience: 0.00750254141167
mentions {
  text {
    content: "programming paradigms"
    begin_offset: -1
  }
  type: COMMON
}
, name: "scales."
type: OTHER
salience: 0.00745778018609
mentions {
  text {
    content: "scales."
    begin_offset: -1
  }
  type: COMMON
}
, name: "Guido van Rossum"
type: PERSON
metadata {
  key: "mid"
  value: "/m/01h05c"
}
metadata {
  key: "wikipedia_url"
  value: "https://en.wikipedia.org/wiki/Guido_van_Rossum"
}
salience: 0.00657201046124
mentions {
  text {
    content: "Guido van Rossum"
    begin_offset: -1
  }
  type: PROPER
}
, name: "development model"
type: OTHER
salience: 0.00517438072711
mentions {
  text {
    content: "development model"
    begin_offset: -1
  }
  type: COMMON
}
, name: "all"
type: OTHER
salience: 0.00457722740248
mentions {
  text {
    content: "all"
    begin_offset: -1
  }
  type: COMMON
}
, name: "variant implementations"
type: OTHER
salience: 0.00412607658654
mentions {
  text {
    content: "variant implementations"
    begin_offset: -1
  }
  type: COMMON
}
, name: "operating systems"
type: OTHER
salience: 0.00259233964607
mentions {
  text {
    content: "operating systems"
    begin_offset: -1
  }
  type: COMMON
}
, name: "Python interpreters"
type: PERSON
salience: 0.00222200364806
mentions {
  text {
    content: "Python interpreters"
    begin_offset: -1
  }
  type: COMMON
}
, name: "Python Software Foundation"
type: ORGANIZATION
metadata {
  key: "mid"
  value: "/m/033l1p"
}
metadata {
  key: "wikipedia_url"
  value: "https://en.wikipedia.org/wiki/Python_Software_Foundation"
}
salience: 0.00214090500958
mentions {
  text {
    content: "Python Software Foundation"
    begin_offset: -1
  }
  type: PROPER
}
]