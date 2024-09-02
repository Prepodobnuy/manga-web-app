import axios from 'axios'

async function getTitlesDataByText(numberOfTitles, text) {
  let a = [
    {
      title: {
        id: 123,
        metadata: {
          author: 'debil',
          publisher: 'loh',
          titles: {
            ruTitle: 'ФЫВФЫВФЫВ',
            enTitle: 'ASDASFASF'
          }
        },
        ratings: {
          1: 1,
          2: 1,
          3: 1,
          4: 1,
          5: 1,
          6: 1,
          7: 1,
          8: 1,
          9: 1,
          10: 112
        },
        lists: {
          another: 1,
          droped: 1,
          loved: 1,
          readed: 1,
          reading: 1,
          wouldread: 1
        }
      }
    } * numberOfTitles
  ]
  try {
    const response = await axios.get(`/title/search/?num:${numberOfTitles}?text:${text}`)
    return response.data
  } catch (error) {
    console.error('Error searching titles:', error)
    return a
  }
}
