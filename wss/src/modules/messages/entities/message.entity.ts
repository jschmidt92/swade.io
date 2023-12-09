export class Message {
  constructor(user: string, content: string) {
    this.user = user
    this.content = content
  }

  user: string
  content: string
}
