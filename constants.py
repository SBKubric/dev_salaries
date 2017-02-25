class LanguagesSet:
    @staticmethod
    def get_languages_patterns() -> list:
        return [
            ["c++", "cpp"],
            ["c", ],
            ["c#", ],
            ["sql", ],
            ["java", "android"],
            ["html", "css", "js", "javascript", ],
            ["delphi", ],
            ["pascal", ],
            ["visualbasic", "vb", "basic", ],
            ["php", ],
            ["perl", ],
            ["ada", ],
            ["1с", "1c", ],
            ["python", "py", "python3", "python2", ],
            ["shell", ],
            ["haskell", ],
            ["matlab", ],
            ["mathcad", ],
            ["octave", ],
            ["ruby", ],
            ["go", ],
            ["scala", ],
            ["assembler", "assembley", ],
            ["groovy", ],
            ["lisp", "common lisp", ],
            ["objective-c", "objective", "ios", ],
            ["r", ],
            ["erlang", ],
            ["swift", "ios", ],
            ["fortran", ],
            ["rust", ],
            ["processing", ],
            ["d", ],
            ["sas", ],
            ["cobol", ],
            ["dart", ],
            ["f#", ],
            ["prolog", ],
            ["lua"],
        ]

    @staticmethod
    def get_languages_json_list() -> list:
        return [
            {'lang': "C++", },
            {'lang': "C", },
            {'lang': "C#", },
            {'lang': "SQL", },
            {'lang': "Java|Android", },
            {'lang': "HTML|CSS|JS", },
            {'lang': "Delphi", },
            {'lang': "Pascal", },
            {'lang': "VB", },
            {'lang': "PHP", },
            {'lang': "Perl", },
            {'lang': "Ada", },
            {'lang': "1C", },
            {'lang': "Python", },
            {'lang': "Shell", },
            {'lang': "Haskell", },
            {'lang': "Matlab", },
            {'lang': "Mathcad", },
            {'lang': "Octave", },
            {'lang': "Ruby", },
            {'lang': "Go", },
            {'lang': "Scala", },
            {'lang': "Assembler", },
            {'lang': "Groovy", },
            {'lang': "Lisp", },
            {'lang': "Objective-C", },
            {'lang': "R", },
            {'lang': "Erlang", },
            {'lang': "Swift", },
            {'lang': "FORTRAN", },
            {'lang': "Rust", },
            {'lang': "Processing", },
            {'lang': "D", },
            {'lang': "SAS", },
            {'lang': "COBOL", },
            {'lang': "Dart", },
            {'lang': "F#", },
            {'lang': "Prolog", },
            {'lang': "Lua"},
        ]


    @staticmethod
    def get_languages_statistics_container() -> list:
        langs_json = LanguagesSet.get_languages_json_list()
        langs_statistics_json = [
            {
                'lang': lang['lang'],
                'count': 0,
                'salary': 0,
            } for lang in langs_json
        ]
        return langs_statistics_json
