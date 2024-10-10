import streamlit as st
from langchain_community.document_loaders import YoutubeLoader

st.title('Bakht\'s YouTube Transcriptor')
st.write('Enter a youtube video url for transcription extraction')

#User input for Youtube URL
youtube_url = st.text_input('Youtube URL', "")
if st.button('Load Video'):
    if youtube_url:
        try:
            loader = YoutubeLoader.from_youtube_url(youtube_url, add_video_info = True)
            documents = loader.load()

            #Video Information
            st.subheader('Video Metadata')
            st.write(f'Title: {documents[0].metadata.get('title', 'N/A')}')
            st.write(f'Description: {documents[0].metadata.get('description', 'N/A')}')
            st.write(f'Channel: {documents[0].metadata.get('channel', 'N/A')}')
            st.write(f'Published Date: {documents[0].metadata.get('publish_date', 'N/A')}')
            st.write(f'View Count: {documents[0].metadata.get('view_count', 'N/A')}')

            #Display the video transcription
            st.subheader('Video Transcription')
            for doc in documents:
                st.write(doc.page_content)
        except:
            st.error('Something went wrong!')
    else:
        st.warning('Please enter the Youtube URL.')
