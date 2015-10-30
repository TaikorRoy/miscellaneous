package com.roy_scala.util

import IO.FileIO._
import scala.util.parsing.json.JSON

/**
 * Created by roy on 2015/10/22.
 */

object json {
  def parse_json_from_file(pth: String): Any =
    {
      val json_str = read(pth)
      val json_parsed = JSON.parseFull(json_str)
      val return_val = json_parsed match {
        // Matches if jsonStr is valid JSON and represents a Map of Strings to Any
        case Some(map: Map[Any, Any]) => map
        case Some(list: List[Any]) => list
        case None => println("Parsing failed"); None
        case other => println("Unknown data structure: " + other); None
      }
      return_val
    }

  def parse_json_from_str(json_str: String): Any =
    {
      val json_parsed = JSON.parseFull(json_str)
      val return_val = json_parsed match {
        // Matches if jsonStr is valid JSON and represents a Map of Strings to Any
        case Some(map: Map[Any, Any]) => map
        case Some(list: List[Any]) => list
        case None => println("Parsing failed"); None
        case other => println("Unknown data structure: " + other); None
      }
      return_val
    }

}
