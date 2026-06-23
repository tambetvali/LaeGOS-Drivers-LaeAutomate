well now the last one "cogenerator.py".

This uses all the files, and now:
- Scans the numbered subfolders, such as "0.5", "1", "2", "3", "4" - you see floats are supported, but keep them as strings as-is because 0.5 should not be 0.4999 to still find or create the right folder.
- Inside it finds the json files. It creates necessarily "U_....json" files itself, as in task for laejson, confirm!

You import all three files, every necessary feature.

Below is content of LIE.json:
- Main index is point number - for two digits "I" and "E", there are points with indexes "1" and "2", one for linear segment; prefix "L" is removed by you from your own file names, one more safe difference beyond addition of "U_" or "?_" prefixed, where ? is I, O, A or E.
- You find 1 and 2 are indexes.
- This is complicated that indexes are main components and below, there are 4 formats.
  - "Signed Ten", which needs, before final ".json", ".png", "csv" or ".svg" suffix, "_st", so that "LIE.json" becomes many files like "U_IE_st.svg", "A_IE_st.png" etc, all in the same convention automatically: png is 5, svg is 5, total 10, and csv, json add 2, total 12, and original file was 1, total 13 - 3 additional formats which come after this bullet add 12*3=36, so the result is 49 files!
- "UnSigned Ten", where you need to add "_ut" suffix and all the same files.
- "Signed Dec", where you add "_sd" suffix.
- "UnSigned Dec", where you add "_ud" suffix.
- Each format adds 12 files to initial file, which remains like single joker in card pack.
- Finally generate README.md, where you add each point coordinates in subchapter, where main chapter contains the laegna number such as "IE", and chapters "I" and "E" contain points based on each digit, which follow the exponent growth production.
- Each point also contains same-named subchapter with *simpler ordering convention*, where each line is separate. Automatically confirm that those equal, as an unit test, or generate based on simpler convention.

So the script:
- Scans folders which corresponds to number length
- Scans files which correspond to numbers
- Regenerates like 48 new files of various formats.
- Records important activities in "gen_record.md", using full md syntax and making claims such as "AA has 5 points" under chapter "AA", when "AA" is added.
- For each R, calculate minimum of upper, minimum of left, maximum of lower and maximum of right, i.e. rather on X and Y, from smaller to bigger numbers, so that you get the image box; give it to number range in it's original coordinates, and in SVG and png pixel coordinates.

Confirm that SVG also, assumes that coordinate of pixel 1, 1 is actually 0.5, 0.5, because it's *still* a discrete coordinate in square grid - if not, you dont need to fix the driver, but simply conver 1, 1 to 0.5, 0.5, 2, 7 to 1.5, 6.5, and so on consistently.

Make it fluent: execute the script, it reads the source jsons and generates their *conversions*. You could better name it "converter.py", because this follows my convention!!

This is content of "LIE.json", and you see it knows it's index even inside, based on content:

{
    "1": {
        "Ten": {
            "Signed": {
                "SrcAxeY": "Axes.UnSignedTen[\"1\"]",
                "SrcY": "Axes.UnSignedTen[\"1\"][\"I\"]",
                "X": 1,
                "Y": -2
            },
            "UnSigned": {
                "SrcAxeY": "Axes.SignedTen[\"1\"]",
                "SrcY": "Axes.SignedTen[\"1\"][\"I\"]",
                "X": 2,
                "Y": 1
            }
        },
        "Id": 1,
        "Dec": {
            "Signed": {
                "SrcAxeY": "Axes.UnSignedDec[\"1\"]",
                "SrcY": "Axes.UnSignedDec[\"1\"][\"I\"]",
                "X": 1,
                "Y": -2
            },
            "UnSigned": {
                "SrcAxeY": "Axes.SignedDec[\"1\"]",
                "SrcY": "Axes.SignedDec[\"1\"][\"I\"]",
                "X": 2,
                "Y": 1
            }
        },
        "1": {
            "Ten": {
                "Signed": {
                    "Ten": {
                        "X": 1,
                        "Y": -2
                    },
                    "Id": {
                        "X": 1,
                        "Y": -2
                    },
                    "Dec": {
                        "X": 1,
                        "Y": -2
                    }
                },
                "UnSigned": {
                    "Ten": {
                        "X": 2,
                        "Y": 1
                    },
                    "Id": {
                        "X": 2,
                        "Y": 1
                    },
                    "Dec": {
                        "X": 2,
                        "Y": 1
                    }
                }
            },
            "Dec": {
                "Signed": {
                    "Ten": {
                        "X": 1,
                        "Y": -2
                    },
                    "Id": {
                        "X": 1,
                        "Y": -2
                    },
                    "Dec": {
                        "X": 1,
                        "Y": -2
                    }
                },
                "UnSigned": {
                    "Ten": {
                        "X": 2,
                        "Y": 1
                    },
                    "Id": {
                        "X": 2,
                        "Y": 1
                    },
                    "Dec": {
                        "X": 2,
                        "Y": 1
                    }
                }
            }
        }
    },
    "2": {
        "Ten": {
            "Signed": {
                "SrcAxeY": "Axes.UnSignedTen[\"2\"]",
                "SrcY": "Axes.UnSignedTen[\"2\"][\"IE\"]",
                "X": 2,
                "Y": -5
            },
            "UnSigned": {
                "SrcAxeY": "Axes.SignedTen[\"2\"]",
                "SrcY": "Axes.SignedTen[\"2\"][\"IE\"]",
                "X": 4,
                "Y": 4
            }
        },
        "Id": 2,
        "Dec": {
            "Signed": {
                "SrcAxeY": "Axes.UnSignedDec[\"2\"]",
                "SrcY": "Axes.UnSignedDec[\"2\"][\"IE\"]",
                "X": 2,
                "Y": -3
            },
            "UnSigned": {
                "SrcAxeY": "Axes.SignedDec[\"2\"]",
                "SrcY": "Axes.SignedDec[\"2\"][\"IE\"]",
                "X": 4,
                "Y": 6
            }
        },
        "2": {
            "Ten": {
                "Signed": {
                    "Ten": {
                        "X": 2,
                        "Y": -5
                    },
                    "Id": {
                        "X": 2,
                        "Y": -5
                    },
                    "Dec": {
                        "X": 2,
                        "Y": -5
                    }
                },
                "UnSigned": {
                    "Ten": {
                        "X": 4,
                        "Y": 4
                    },
                    "Id": {
                        "X": 4,
                        "Y": 4
                    },
                    "Dec": {
                        "X": 4,
                        "Y": 4
                    }
                }
            },
            "Dec": {
                "Signed": {
                    "Ten": {
                        "X": 2,
                        "Y": -3
                    },
                    "Id": {
                        "X": 2,
                        "Y": -3
                    },
                    "Dec": {
                        "X": 2,
                        "Y": -3
                    }
                },
                "UnSigned": {
                    "Ten": {
                        "X": 4,
                        "Y": 6
                    },
                    "Id": {
                        "X": 4,
                        "Y": 6
                    },
                    "Dec": {
                        "X": 4,
                        "Y": 6
                    }
                }
            }
        }
    }
}