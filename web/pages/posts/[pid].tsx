import React from 'react';

import { PostPage } from '../../components/PostPage/PostPage';
import { GetServerSideProps, InferGetServerSidePropsType } from "next";
import {getPost, getPostComments} from "../../services";


export const getServerSideProps: GetServerSideProps = async (context) => {
    const { params } = context;
    const postID = params.pid;
    const post = await getPost(postID as string);
    const comments = await getPostComments(postID as string);
    return {
        props: {
            post,
            comments,
        }
    }
};


const Pid = ({post, comments}: InferGetServerSidePropsType<typeof getServerSideProps>) => {
    return <PostPage post={post} comments={comments}/>
};


export default Pid;