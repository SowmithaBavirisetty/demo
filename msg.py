def slackResponse = slackSend(channel: "testslack_euh", message: "Here is the primary message") :
  slackSend(channel: slackResponse.threadId, message: "Thread reply #1")
  slackSend(channel: slackResponse.threadId, message: "Thread reply #2")
